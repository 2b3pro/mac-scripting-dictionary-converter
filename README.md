# sdef-converter

This project provides a Python script (`sdef_to_markdown.py`) to convert Apple's Scripting Definition (.sdef) files into a single, optimized Markdown file. This Markdown output includes a table of contents, YAML front matter for each definition, and structured tables for properties, parameters, and enumerators, making it easier to read and navigate scripting dictionaries.

## Usage

To use the script, you need to provide the path to an `.sdef` file and the desired output Markdown file path.

```bash
python sdef_to_markdown.py <path_to_sdef_file> <output_file.md>
```

**Example:**

```bash
python sdef_to_markdown.py dictionaries/DEVONthink.sdef DEVONthink_Scripting_Dictionary.md
```

### Help Feature

To display the usage instructions, run:

```bash
python sdef_to_markdown.py --help
```

## `scriptsuite_to_markdown.py`

This script converts Apple's `.scriptSuite` and `.scriptTerminology` files (often found within application bundles alongside `.sdef` files) into a single, structured Markdown file. It extracts commands, classes, properties, and elements, presenting them with descriptions, types, and usage details. This is particularly useful for applications that provide their scripting dictionaries in this format, such as DEVONagent.

### Usage

To use this script, you need to provide the paths to the `.scriptSuite` file, the `.scriptTerminology` file, and the desired output Markdown file path.

```bash
python scriptsuite_to_markdown.py <path_to_scriptSuite_file> <path_to_scriptTerminology_file> <output_file.md>
```

**Example:**

```bash
python scriptsuite_to_markdown.py dictionaries/DEVONagent.scriptSuite dictionaries/DEVONagent.scriptTerminology DEVONagent_Scripting_Dictionary.md
```

### Help Feature

To display the usage instructions, run:

```bash
python scriptsuite_to_markdown.py --help
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
