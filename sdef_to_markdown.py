import xml.etree.ElementTree as ET
import os
import re
import html

def sanitize_filename(name):
    """Sanitizes a string to be used as a valid filename."""
    if not name:
        return "_unknown_"
    return re.sub(r'[^a-zA-Z0-9_-]', '_', name)

def generate_anchor(name):
    """Generates a markdown anchor link from a string."""
    return sanitize_filename(name).lower()

def get_types(element):
    """Extracts type information from an element."""
    types = [t.get('type') for t in element.findall('type')]
    if element.get('type'):
        types.insert(0, element.get('type'))
    return list(filter(None, types))

def parse_sdef_to_optimized_markdown(sdef_path, output_file):
    """
    Parses an SDEF file and creates a single, optimized markdown file with a TOC, YAML front matter, and tables.
    """
    try:
        tree = ET.parse(sdef_path)
    except ET.ParseError:
        with open(sdef_path, 'r', encoding='utf-8') as f:
            xml_content = f.read()
        xml_content = re.sub(r'<!DOCTYPE[^>]*>', '', xml_content)
        root = ET.fromstring(xml_content)
    else:
        root = tree.getroot()

    dictionary_title = root.get('title', 'Application')
    title = f"# {dictionary_title}: AppleScript/JSX\n\n"

    toc = "## Table of Contents\n\n"
    main_content = ""

    for suite in root.findall('suite'):
        suite_name = suite.get('name')
        toc += f"### {suite_name}\n"
        main_content += f"## {suite_name}\n\n"
        main_content += f"**Description:** {suite.get('description')}\n\n"

        documentation = suite.find('documentation')
        if documentation is not None:
            html_element = documentation.find('html')
            if html_element is not None:
                main_content += "### Sample Code\n"
                html_content_str = ET.tostring(html_element, encoding='unicode', method='html')
                matches = re.findall(r"<p><i>(.*?)</i></p>.*?<pre>\s*(.*?)\s*</pre>", html_content_str, re.DOTALL)
                for lang, code in matches:
                    lang_name = lang.replace(':', '').strip().lower()
                    main_content += f"```{lang_name}\n{html.unescape(code)}\n```\n\n"

        for element_type in ['command', 'class', 'enumeration', 'record-type', 'value-type', 'class-extension']:
            elements = suite.findall(element_type)
            if elements:
                toc += f"#### {element_type.replace('-', ' ').title()}s\n"
                for element in elements:
                    name = element.get('name') or element.get('extends')
                    anchor = generate_anchor(name)
                    toc += f"- [{name}](#{anchor})\n"

                    main_content += f"---\n\n"
                    main_content += f"<a name=\"{anchor}\"></a>\n"

                    # YAML Front Matter
                    main_content += f"```yaml\n"
                    main_content += f"type: {element_type}\n"
                    main_content += f"name: {name}\n"
                    main_content += f"suite: {suite_name}\n"
                    main_content += f"---\n\n"

                    main_content += f"## {element_type.replace('-', ' ').title()}: {name}\n\n"

                    if element.get('description'):
                        main_content += f"**Description:** {element.get('description')}\n\n"
                    if element.get('inherits'):
                        main_content += f"**Inherits:** {element.get('inherits')}\n\n"

                    documentation = element.find('documentation')
                    if documentation is not None:
                        html_element = documentation.find('html')
                        if html_element is not None:
                            main_content += "### Sample Code\n"
                            html_content_str = ET.tostring(html_element, encoding='unicode', method='html')
                            matches = re.findall(r"<p><i>(.*?)</i></p>.*?<pre>\s*(.*?)\s*</pre>", html_content_str, re.DOTALL)
                            for lang, code in matches:
                                lang_name = lang.replace(':', '').strip().lower()
                                main_content += f"```{lang_name}\n{html.unescape(code)}\n```\n\n"

                    if element_type == 'command':
                        direct_param = element.find('direct-parameter')
                        if direct_param is not None:
                            main_content += "### Direct Parameter\n"
                            if direct_param.get('description'):
                                main_content += f"- **Description:** {direct_param.get('description')}\n"
                            types = get_types(direct_param)
                            if types:
                                main_content += f"- **Types:** {', '.join(types)}\n"

                        parameters = element.findall('parameter')
                        if parameters:
                            main_content += "### Parameters\n"
                            main_content += "| Name | Description | Type | Optional |\n"
                            main_content += "|---|---|---|---|\n"
                            for param in parameters:
                                param_name = param.get('name', '')
                                description = param.get('description', '')
                                types = ", ".join(get_types(param))
                                optional = 'Yes' if param.get('optional') == 'yes' else 'No'
                                main_content += f"| {param_name} | {description} | {types} | {optional} |\n"
                            main_content += "\n"

                        result = element.find('result')
                        if result is not None:
                            main_content += "### Result\n"
                            if result.get('description'):
                                main_content += f"- **Description:** {result.get('description')}\n"
                            types = get_types(result)
                            if types:
                                main_content += f"- **Types:** {', '.join(types)}\n"

                    if element_type in ['class', 'record-type', 'class-extension']:
                        properties = element.findall('property')
                        if properties:
                            main_content += "### Properties\n"
                            main_content += "| Name | Description | Type | Access |\n"
                            main_content += "|---|---|---|---|\n"
                            for prop in properties:
                                prop_name = prop.get('name', '')
                                description = prop.get('description', '')
                                types = ", ".join(get_types(prop))
                                access = prop.get('access', 'read/write')
                                main_content += f"| {prop_name} | {description} | {types} | {access} |\n"
                            main_content += "\n"

                        elements = element.findall('element')
                        if elements:
                            main_content += "### Elements\n"
                            for elem in elements:
                                 main_content += f"- **Type:** {elem.get('type')}\n"

                        responds_to = element.findall('responds-to')
                        if responds_to:
                            main_content += "### Responds To\n"
                            for rt in responds_to:
                                main_content += f"- **Command:** {rt.get('command')}\n"

                    if element_type == 'enumeration':
                        enumerators = element.findall('enumerator')
                        if enumerators:
                            main_content += "### Enumerators\n"
                            main_content += "| Name | Description |\n"
                            main_content += "|---|---|\n"
                            for enumerator in enumerators:
                                main_content += f"| {enumerator.get('name')} | {enumerator.get('description')} |\n"
                            main_content += "\n"

                    xrefs = element.findall('xref')
                    if xrefs:
                        main_content += "### See Also\n"
                        for xref in xrefs:
                            target = xref.get('target')
                            if target:
                                main_content += f"- [{target}](#{generate_anchor(target)})\n"

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(title + toc + "\n\n" + main_content)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print("Usage: python sdef_to_markdown.py <path_to_sdef_file> <output_file>")
        print("       Use --help for more information.")
        sys.exit(0)
    if len(sys.argv) != 3:
        print("Error: Incorrect number of arguments.")
        print("Usage: python sdef_to_markdown.py <path_to_sdef_file> <output_file>")
        sys.exit(1)
    sdef_file = sys.argv[1]
    output_file = sys.argv[2]
    parse_sdef_to_optimized_markdown(sdef_file, output_file)
    print(f"Optimized markdown file generated: {output_file}")