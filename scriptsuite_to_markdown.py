import re
import html
import sys

def sanitize_filename(name):
    """Sanitizes a string to be used as a valid filename."""
    if not name:
        return "_unknown_"
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def generate_anchor(name):
    """Generates a markdown anchor link from a string."""
    return sanitize_filename(name).lower()

def map_type(type_str):
    """Maps internal type strings to more readable ones."""
    type_map = {
        "NSString": "text",
        "NSNumber": "number",
        "NSNumber<Bool>": "boolean",
        "NSNumber<Int>": "integer",
        "NSNumber<Float>": "real",
        "NSData<Binary>": "raw data",
        "NSDictionary": "dictionary",
        "NSArray": "list",
        "NSDate": "date",
        "BrowserTab": "browser tab",
        "BrowserWindow": "browser window",
        "QueryWindow": "query window",
        "RecordItem": "record item",
        "NSTextSuite.NSTextStorage": "rich text",
        "****": "raw data", # Common for generic binary data
        "utxt": "text", # AppleEventCode for Unicode text
        "ctxt": "rich text", # AppleEventCode for styled text
        "bool": "boolean", # AppleEventCode for boolean
        "list": "list", # AppleEventCode for list
        "reco": "record", # AppleEventCode for record
    }
    return type_map.get(type_str, type_str)

def parse_nextstep_plist_string(text):
    """
    Parses a simplified NeXTSTEP/ASCII plist string into a Python dictionary.
    Handles dictionaries {}, arrays (), and basic key-value pairs.
    Does NOT handle comments, complex string escaping, or advanced types.
    """
    # Remove comments (// and /* */) and newlines for easier tokenization
    text = re.sub(r'//.*\n', '', text)
    text = re.sub(r'/\*.*?\*/', '', text, flags=re.DOTALL)
    text = text.replace('\n', '').replace('\t', '').strip()

    # Tokenize the string
    # Matches: quoted strings, unquoted words (keys/values), and structural characters
    tokens = re.findall(r'"(?:\\"|[^\"])*"|[a-zA-Z_][a-zA-Z0-9_.]*|[{}();=,]', text)

    # Add a sentinel to avoid index out of bounds errors at the end of parsing
    tokens.append('END')

    current_index = 0

    # print(f"DEBUG: Initial tokens: {tokens}") # DEBUG

    def parse_value():
        nonlocal current_index
        token = tokens[current_index]

        if token == '{':
            current_index += 1
            return parse_dict()
        elif token == '(':
            current_index += 1
            return parse_array()
        elif token == 'YES':
            current_index += 1
            return True
        elif token == 'NO':
            current_index += 1
            return False
        elif token.startswith('"') and token.endswith('"'):
            current_index += 1
            return token[1:-1].replace('"', '"')
        else:
            # Try to convert to number, otherwise keep as string
            try:
                value = int(token)
            except ValueError:
                try:
                    value = float(token)
                except ValueError:
                    value = token
            current_index += 1
            return value

    def parse_dict():
        nonlocal current_index
        result = {}
        # print(f"DEBUG: Entering parse_dict. current_index={current_index}, token={tokens[current_index]}") # DEBUG
        while tokens[current_index] != '}' and tokens[current_index] != 'END':
            key = tokens[current_index]
            current_index += 1
            # print(f"DEBUG: In parse_dict, after key. current_index={current_index}, token={tokens[current_index]}") # DEBUG
            # Check if the next token is '=' for simple key-value, or '{' for nested dict, or '(' for array
            if tokens[current_index] == '=':
                current_index += 1
                value = parse_value() # parse_value will handle nested dicts/arrays
                result[key] = value
            elif tokens[current_index] == '{': # Nested dictionary
                value = parse_dict() # Recursively parse the nested dictionary
                result[key] = value
            elif tokens[current_index] == '(': # Nested array
                value = parse_array() # Recursively parse the nested array
                result[key] = value
            else:
                raise ValueError(f"Expected '=', '{{', or '(' at index {current_index}, got {tokens[current_index]}")

            if tokens[current_index] == ';': # Consume semicolon if present
                current_index += 1
        current_index += 1 # Consume '}'
        return result

    def parse_array():
        nonlocal current_index
        result = []
        # print(f"DEBUG: Entering parse_array. current_index={current_index}, token={tokens[current_index]}") # DEBUG
        while tokens[current_index] != ')' and tokens[current_index] != 'END':
            value = parse_value()
            result.append(value)
            if tokens[current_index] == ',':
                current_index += 1
        current_index += 1 # Consume ')'
        return result

    # Start parsing from the root dictionary
    if not tokens or tokens[0] != '{':
        raise ValueError("Invalid plist format: Root must be a dictionary.")

    # Initial call to parse_dict for the root, starting after the initial '{'
    current_index += 1 # Consume the initial '{'
    return parse_dict()

def parse_script_suite_to_markdown(suite_path, terminology_path, output_file):
    """
    Parses .scriptSuite and .scriptTerminology files and creates a single markdown file.
    """
    try:
        with open(suite_path, 'r', encoding='utf-8') as fp:
            suite_data = parse_nextstep_plist_string(fp.read())
        with open(terminology_path, 'r', encoding='utf-8') as fp:
            terminology_data = parse_nextstep_plist_string(fp.read())
    except Exception as e:
        print(f"Error loading plist files: {e}")
        sys.exit(1)

    dictionary_title = terminology_data.get('Name', 'Application')
    suite_name = terminology_data.get('Name', 'Unknown Suite')
    suite_description = terminology_data.get('Description', '')

    title = f"# {dictionary_title}: AppleScript/JSX Dictionary\n\n"

    toc = "## Table of Contents\n\n"
    main_content = ""

    # Suite Header
    main_content += f"## {suite_name}\n\n"
    if suite_description:
        main_content += f"**Description:** {suite_description}\n\n"

    # Process Commands
    if 'Commands' in suite_data:
        toc += f"### Commands\n"
        main_content += f"### Commands\n"
        for cmd_id, cmd_suite_info in suite_data['Commands'].items():
            cmd_term_info = terminology_data['Commands'].get(cmd_id, {})
            name = cmd_term_info.get('Name', cmd_id)
            description = cmd_term_info.get('Description', '')
            anchor = generate_anchor(name)

            toc += f"- [{name}](#{anchor})\n"

            main_content += f'<a name="{anchor}"></a>\n'
            main_content += f"```yaml\n"
            main_content += f"---\n"
            main_content += f"type: command\n"
            main_content += f"name: {name}\n"
            main_content += f"suite: {suite_name}\n"
            main_content += f"---\n```\n\n"
            main_content += f"## Command: {name}\n\n"
            if description:
                main_content += f"**Description:** {description}\n\n"

            # Unnamed Argument (Direct Parameter)
            unnamed_arg_suite = cmd_suite_info.get('UnnamedArgument')
            unnamed_arg_term = cmd_term_info.get('UnnamedArgument')
            if unnamed_arg_suite:
                main_content += "### Direct Parameter\n"
                if unnamed_arg_term and unnamed_arg_term.get('Description'):
                    main_content += f"- **Description:** {unnamed_arg_term['Description']}\n"
                main_content += f"- **Types:** {map_type(unnamed_arg_suite.get('Type', ''))}\n"
                main_content += f"- **Optional:** {'Yes' if unnamed_arg_suite.get('Optional') else 'No'}\n"

            # Arguments (Parameters)
            args_suite = cmd_suite_info.get('Arguments', {})
            args_term = cmd_term_info.get('Arguments', {})
            if args_suite:
                main_content += "### Parameters\n"
                main_content += "| Name | Description | Type | Optional |\n"
                main_content += "|---|---|---|---|\n" # Do not change this line
                for arg_id, arg_suite_info in args_suite.items():
                    arg_term_info = args_term.get(arg_id, {})
                    arg_name = arg_term_info.get('Name', arg_id)
                    arg_description = arg_term_info.get('Description', '')
                    arg_type = map_type(arg_suite_info.get('Type', ''))
                    arg_optional = 'Yes' if arg_suite_info.get('Optional') else 'No'
                    main_content += f"| {arg_name} | {arg_description} | {arg_type} | {arg_optional} |\n"
                main_content += "\n"

            # Result
            result_type = cmd_suite_info.get('ResultAppleEventCode') or cmd_suite_info.get('Type')
            if result_type:
                main_content += "### Result\n"
                main_content += f"- **Types:** {map_type(result_type)}\n"

    # Process Classes
    if 'Classes' in suite_data:
        toc += f"### Classes\n"
        main_content += f"### Classes\n"
        for class_id, class_suite_info in suite_data['Classes'].items():
            class_term_info = terminology_data['Classes'].get(class_id, {})
            name = class_term_info.get('Name', class_id)
            description = class_term_info.get('Description', '')
            anchor = generate_anchor(name)

            toc += f"- [{name}](#{anchor})\n"

            main_content += f'<a name="{anchor}"></a>\n'
            main_content += f"```yaml\n"
            main_content += f"type: class\n"
            main_content += f"---\n"
            main_content += f"name: {name}\n"
            main_content += f"suite: {suite_name}\n"
            main_content += f"---\n```\n\n"
            main_content += f"## Class: {name}\n\n"
            if description:
                main_content += f"**Description:** {description}\n\n"

            if 'Superclass' in class_suite_info:
                main_content += f"**Inherits:** {class_suite_info['Superclass']}\n\n"

            # Attributes (Properties)
            attributes_suite = class_suite_info.get('Attributes', {})
            attributes_term = class_term_info.get('Attributes', {})
            if attributes_suite:
                main_content += "### Properties\n"
                main_content += "| Name | Description | Type | Access |\n"
                main_content += "|---|---|---|---|\n" # Do not change this line
                for attr_id, attr_suite_info in attributes_suite.items():
                    attr_term_info = attributes_term.get(attr_id, {})
                    attr_name = attr_term_info.get('Name', attr_id)
                    attr_description = attr_term_info.get('Description', '')
                    attr_type = map_type(attr_suite_info.get('Type', ''))
                    access = 'read/write' # Default, as not explicitly stated in these files
                    if attr_suite_info.get('ReadOnly'):
                        access = 'read only'
                    main_content += f"| {attr_name} | {attr_description} | {attr_type} | {access} |\n"
                main_content += "\n"

            # ToManyRelationships (Elements)
            relationships_suite = class_suite_info.get('ToManyRelationships', {})
            if relationships_suite:
                main_content += "### Elements\n"
                for rel_id, rel_suite_info in relationships_suite.items():
                    main_content += f"- **Type:** {map_type(rel_suite_info.get('Type', ''))}\n"

            # SupportedCommands (Responds To)
            supported_commands = class_suite_info.get('SupportedCommands', {})
            if supported_commands:
                main_content += "### Responds To\n"
                for cmd_name, _ in supported_commands.items():
                    # Clean up command name if it includes suite prefix
                    clean_cmd_name = cmd_name.split('.')[-1] # e.g., "NSCoreSuite.Close" -> "Close"
                    main_content += f"- **Command:** {clean_cmd_name}\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(title + toc + "\n\n" + main_content)

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print("Usage: python scriptsuite_to_markdown.py <path_to_scriptSuite_file> <path_to_scriptTerminology_file> <output_file>")
        print("       Use --help for more information.")
        sys.exit(0)
    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments.")
        print("Usage: python scriptsuite_to_markdown.py <path_to_scriptSuite_file> <path_to_scriptTerminology_file> <output_file>")
        sys.exit(1)

    suite_file = sys.argv[1]
    terminology_file = sys.argv[2]
    output_file = sys.argv[3]

    parse_script_suite_to_markdown(suite_file, terminology_file, output_file)
    print(f"Markdown file generated: {output_file}")
