# Mac Scripting Dictionary Converter

This project offers Python scripts to convert Apple's macOS application scripting dictionaries (.sdef, .scriptSuite, and .scriptTerminology files) into well-structured Markdown documentation. This conversion simplifies the process of understanding and navigating complex scripting interfaces, making them more accessible for developers and automation enthusiasts.

The generated Markdown files include:
- A comprehensive table of contents.
- YAML front matter for each definition, enabling easy parsing and integration with other tools.
- Structured tables detailing properties, parameters, and enumerators.
- Any available sample code, enhancing practical understanding.

## Usage

This project includes two distinct scripts for converting different types of scripting dictionary files.

### `sdef_to_markdown.py`

Converts modern Apple Scripting Definition (`.sdef`) files into Markdown.

**Syntax:**
```bash
python sdef_to_markdown.py <path_to_sdef_file> <output_file.md>
```

**Example:**
```bash
python sdef_to_markdown.py dictionaries/DEVONthink.sdef DEVONthink_Scripting_Dictionary.md
```

### `scriptsuite_to_markdown.py`

Converts older Apple `.scriptSuite` and `.scriptTerminology` files (often found alongside `.sdef` files within application bundles) into Markdown.

**Syntax:**
```bash
python scriptsuite_to_markdown.py <path_to_scriptSuite_file> <path_to_scriptTerminology_file> <output_file.md>
```

**Example:**
```bash
python scriptsuite_to_markdown.py dictionaries/DEVONagent.scriptSuite dictionaries/DEVONagent.scriptTerminology DEVONagent_Scripting_Dictionary.md
```

### Getting Help

For detailed usage instructions for either script, use the `--help` flag:
```bash
python <script_name>.py --help
```

## Finding .sdef Files on macOS

`.sdef` files are typically located inside macOS application bundles. Here's how you can usually find them:

1.  **Locate the Application:** Find the application in your `Applications` folder (or wherever it's installed).
2.  **Show Package Contents:** Right-click (or Control-click) on the application icon and select "Show Package Contents". This will open a new Finder window showing the internal structure of the application bundle.
3.  **Navigate to Resources:** Inside the package, navigate to the `Contents` folder, and then usually into the `Resources` folder.
4.  **Search for .sdef:** Look for files ending with the `.sdef` extension. They are often named after the application or a specific component (e.g., `DEVONthink.sdef`, `Finder.sdef`).

    *Common paths include:*
    *   `<ApplicationName>.app/Contents/Resources/*.sdef`
    *   `<ApplicationName>.app/Contents/Frameworks/<FrameworkName>.framework/Resources/*.sdef`

Once you find the `.sdef` file, you can drag and drop it into your terminal to get its full path, or manually copy the path.

## Output Markdown Structure

The generated Markdown file will have the following structure:

*   **Title**: The dictionary title (e.g., "Application: AppleScript/JSX").
*   **Table of Contents**: A hierarchical table of contents linking to suites and their contained elements (commands, classes, etc.).
*   **Suites**: Each suite will have a heading, description, and any sample code found.
*   **Elements (Commands, Classes, etc.)**: Each element will start with YAML front matter containing its type, name, and suite. This is followed by a detailed section including:
    *   Description
    *   Inheritance information (if applicable)
    *   Sample code (if available)
    *   Tables for parameters, properties, and enumerators.
    *   "See Also" links for cross-references.

## Dependencies

This script uses standard Python libraries and does not require any external installations:

*   `xml.etree.ElementTree`
*   `os`
*   `re`
*   `html`

## Keywords

- LLM
- data preparation
- scripting dictionary
- AppleScript
- JavaScript
- tool
- automation
- metadata
- documentation
