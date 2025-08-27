# OmniOutliner Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [open](#open)
- [close](#close)
- [save](#save)
- [print](#print)
- [quit](#quit)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [make](#make)
- [move](#move)
- [GetURL](#geturl)
#### Classs
- [application](#application)
- [document](#document)
- [window](#window)
#### Enumerations
- [save options](#save_options)
- [printing error handling](#printing_error_handling)
#### Record Types
- [print settings](#print_settings)
### OmniOutliner suite
#### Commands
- [collapseAll](#collapseall)
- [expandAll](#expandall)
- [expel ancestors](#expel_ancestors)
- [expel descendants](#expel_descendants)
- [format tokens](#format_tokens)
- [get parameter](#get_parameter)
- [group](#group)
- [ungroup](#ungroup)
- [hoist](#hoist)
- [unhoist](#unhoist)
- [import](#import)
- [export](#export)
- [indent](#indent)
- [outdent](#outdent)
- [open with results](#open_with_results)
- [organize](#organize)
- [redo](#redo)
- [set parameter](#set_parameter)
- [undo](#undo)
- [evaluate javascript](#evaluate_javascript)
- [select](#select)
- [pbcopy](#pbcopy)
- [pbpaste](#pbpaste)
- [pbsave](#pbsave)
#### Classs
- [document type](#document_type)
- [readable document type](#readable_document_type)
- [writable document type](#writable_document_type)
- [row](#row)
- [child](#child)
- [ancestor](#ancestor)
- [section](#section)
- [selected row](#selected_row)
- [leaf](#leaf)
- [following sibling](#following_sibling)
- [preceding sibling](#preceding_sibling)
- [path component](#path_component)
- [level style](#level_style)
- [cell](#cell)
- [column](#column)
- [selected column](#selected_column)
- [conduit setting domain](#conduit_setting_domain)
- [enumeration](#enumeration)
- [xsl transform](#xsl_transform)
#### Enumerations
- [note display type](#note_display_type)
- [sort order type](#sort_order_type)
- [checkbox state](#checkbox_state)
- [column type](#column_type)
- [column summary type](#column_summary_type)
- [text alignment type](#text_alignment_type)
- [format style](#format_style)
#### Record Types
- [column format](#column_format)
#### Class Extensions
- [application](#application)
- [document](#document)
### OmniStyle Scripting
#### Classs
- [style](#style)
- [attribute](#attribute)
- [named style](#named_style)
#### Record Types
- [point](#point)
- [generic color](#generic_color)
#### Value Types
- [color](#color)
- [TIFF data](#tiff_data)
- [PNG data](#png_data)
- [archive data](#archive_data)
### Omni Text Suite
#### Commands
- [insert](#insert)
- [clear](#clear)
#### Classs
- [rich text](#rich_text)
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
- [attribute run](#attribute_run)
- [attachment](#attachment)
- [file attachment](#file_attachment)
### Extended Text Suite
#### Commands
- [bold](#bold)
- [italicize](#italicize)
- [replace](#replace)
- [unbold](#unbold)
- [underline](#underline)
- [unitalicize](#unitalicize)
- [ununderline](#ununderline)
#### Enumerations
- [TextAlignment](#textalignment)
#### Class Extensions
- [rich text](#rich_text)
### OmniFoundation Scripting
#### Commands
- [add](#add)
- [remove](#remove)
#### Classs
- [preference](#preference)


## Standard Suite

**Description:** Common classes and commands for all applications.

<a name="open"></a>
```yaml
---
type: command
name: open
suite: Standard Suite
---
```

## Command: open

**Description:** Open one or more documents.

### Direct Parameter
- **Description:** The file(s) to be opened.
- **Types:** file, file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with properties | Extra properties for use in the open command.  Generally indented for debugging right now (these won't be set on the opened document, for example). | record | Yes |

### Result
- **Description:** The opened document(s).
- **Types:** document, document
<a name="close"></a>
```yaml
---
type: command
name: close
suite: Standard Suite
---
```

## Command: close

**Description:** Close a document.

### Direct Parameter
- **Description:** the document(s) or window(s) to close.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Should changes be saved before closing? | save options | Yes |
| saving in | The file in which to save the document, if so. | file | Yes |

<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
---
```

## Command: save

**Description:** Save a document.

### Direct Parameter
- **Description:** The document(s) or window(s) to save.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file in which to save the document. | file | Yes |
| as | The file format to use. | text | Yes |

<a name="print"></a>
```yaml
---
type: command
name: print
suite: Standard Suite
---
```

## Command: print

**Description:** Print a document.

### Direct Parameter
- **Description:** The file(s), document(s), or window(s) to be printed.
- **Types:** file, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with properties | The print settings to use. | print settings | Yes |
| print dialog | Should the application show the print dialog? | boolean | Yes |

<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: Standard Suite
---
```

## Command: quit

**Description:** Quit the application.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Should changes be saved before quitting? | save options | Yes |

<a name="count"></a>
```yaml
---
type: command
name: count
suite: Standard Suite
---
```

## Command: count

**Description:** Return the number of elements of a particular class within an object.

### Direct Parameter
- **Description:** The objects to be counted.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | The class of objects to be counted. | type | Yes |

### Result
- **Description:** The count.
- **Types:** integer
<a name="delete"></a>
```yaml
---
type: command
name: delete
suite: Standard Suite
---
```

## Command: delete

**Description:** Delete an object.

### Direct Parameter
- **Description:** The object(s) to delete.
- **Types:** specifier, specifier
<a name="duplicate"></a>
```yaml
---
type: command
name: duplicate
suite: Standard Suite
---
```

## Command: duplicate

**Description:** Copy an object.

### Direct Parameter
- **Description:** The object(s) to copy.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new copy or copies. | location specifier | Yes |
| with properties | Properties to set in the new copy or copies right away. | record | Yes |

<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify that an object exists.

### Direct Parameter
- **Description:** The object(s) to check.
- **Types:** any
### Result
- **Description:** Did the object(s) exist?
- **Types:** boolean
<a name="make"></a>
```yaml
---
type: command
name: make
suite: Standard Suite
---
```

## Command: make

**Description:** Create a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object. | type | No |
| at | The location at which to insert the object. | location specifier | Yes |
| with data | The initial contents of the object. | any | Yes |
| with properties | The initial values for properties of the object. | record | Yes |

### Result
- **Description:** The new object.
- **Types:** specifier
<a name="move"></a>
```yaml
---
type: command
name: move
suite: Standard Suite
---
```

## Command: move

**Description:** Move an object to a new location.

### Direct Parameter
- **Description:** The object(s) to move.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new location for the object(s). | location specifier | No |

<a name="geturl"></a>
```yaml
---
type: command
name: GetURL
suite: Standard Suite
---
```

## Command: GetURL

**Description:** Open a document from an URL.

### Direct Parameter
- **Description:** The URL of the file to be opened.
- **Types:** text
<a name="application"></a>
```yaml
---
type: class
name: application
suite: Standard Suite
---
```

## Class: application

**Description:** The application's top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application. | text | r |
| frontmost | Is this the active application? | boolean | r |
| version | The version number of the application. | text | r |

### Elements
- **Type:** document
- **Type:** window
### Responds To
- **Command:** open
- **Command:** print
- **Command:** quit
<a name="document"></a>
```yaml
---
type: class
name: document
suite: Standard Suite
---
```

## Class: document

**Description:** A document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | Its name. | text | r |
| modified | Has it been modified since the last save? | boolean | r |
| file | Its location on disk, if it has one. | file | r |

### Responds To
- **Command:** close
- **Command:** print
- **Command:** save
<a name="window"></a>
```yaml
---
type: class
name: window
suite: Standard Suite
---
```

## Class: window

**Description:** A window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The title of the window. | text | r |
| id | The unique identifier of the window. | integer | r |
| index | The index of the window, ordered front to back. | integer | read/write |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Does the window have a close button? | boolean | r |
| miniaturizable | Does the window have a minimize button? | boolean | r |
| miniaturized | Is the window minimized right now? | boolean | read/write |
| resizable | Can the window be resized? | boolean | r |
| visible | Is the window visible right now? | boolean | read/write |
| zoomable | Does the window have a zoom button? | boolean | r |
| zoomed | Is the window zoomed right now? | boolean | read/write |
| document | The document whose contents are displayed in the window. | document | r |

### Responds To
- **Command:** close
- **Command:** print
- **Command:** save
<a name="save_options"></a>
```yaml
---
type: enumeration
name: save options
suite: Standard Suite
---
```

## Enumeration: save options

### Enumerators
| Name | Description |
|---|---|
| yes | Save the file. |
| no | Do not save the file. |
| ask | Ask the user whether or not to save the file. |

<a name="printing_error_handling"></a>
```yaml
---
type: enumeration
name: printing error handling
suite: Standard Suite
---
```

## Enumeration: printing error handling

### Enumerators
| Name | Description |
|---|---|
| standard | Standard PostScript error handling |
| detailed | print a detailed report of PostScript errors |

<a name="print_settings"></a>
```yaml
---
type: record-type
name: print settings
suite: Standard Suite
---
```

## Record Type: print settings

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| copies | the number of copies of a document to be printed | integer | read/write |
| collating | Should printed copies be collated? | boolean | read/write |
| starting page | the first page of the document to be printed | integer | read/write |
| ending page | the last page of the document to be printed | integer | read/write |
| pages across | number of logical pages laid across a physical page | integer | read/write |
| pages down | number of logical pages laid out down a physical page | integer | read/write |
| requested print time | the time at which the desktop printer should print the document | date | read/write |
| error handling | how errors are handled | printing error handling | read/write |
| fax number | for fax number | text | read/write |
| target printer | for target printer | text | read/write |

## OmniOutliner suite

**Description:** AppleScript commands and classes specific to OmniOutliner.

<a name="collapseall"></a>
```yaml
---
type: command
name: collapseAll
suite: OmniOutliner suite
---
```

## Command: collapseAll

**Description:** Collapse the entire outline.

### Direct Parameter
- **Description:** The rows or documents to collapse completely.
- **Types:** document, document, row, row
<a name="expandall"></a>
```yaml
---
type: command
name: expandAll
suite: OmniOutliner suite
---
```

## Command: expandAll

**Description:** Expand the entire outline.

### Direct Parameter
- **Description:** The rows or documents to expand completely.
- **Types:** document, document, row, row
<a name="expel_ancestors"></a>
```yaml
---
type: command
name: expel ancestors
suite: OmniOutliner suite
---
```

## Command: expel ancestors

**Description:** Given a list of rows, returns a filtered list of rows by removing any row that is a ancestor of another row in the list

### Direct Parameter
- **Description:** The rows to filter.
- **Types:** row, row
### Result
- **Types:** row
<a name="expel_descendants"></a>
```yaml
---
type: command
name: expel descendants
suite: OmniOutliner suite
---
```

## Command: expel descendants

**Description:** Given a list of rows, returns a filtered list of rows by removing any row that is a descendant of another row in the list

### Direct Parameter
- **Description:** The rows to filter.
- **Types:** row, row
### Result
- **Types:** row
<a name="format_tokens"></a>
```yaml
---
type: command
name: format tokens
suite: OmniOutliner suite
---
```

## Command: format tokens

**Description:** Builds a string by evaluation an array of tokens.  Each token can be a string (which evaluates to itself) or a record describing how to build a string.

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
### Result
- **Types:** text
<a name="get_parameter"></a>
```yaml
---
type: command
name: get parameter
suite: OmniOutliner suite
---
```

## Command: get parameter

**Description:** Gets the XPath expression currently set for a XSL parameter

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| named | The name of the parameter | text | No |

### Result
- **Types:** text
<a name="group"></a>
```yaml
---
type: command
name: group
suite: OmniOutliner suite
---
```

## Command: group

**Description:** Increase the outline level of a list of rows by creating a new parent row for them and moving under that new row.

### Direct Parameter
- **Description:** The rows to group.
- **Types:** row, row
### Result
- **Types:** row
<a name="ungroup"></a>
```yaml
---
type: command
name: ungroup
suite: OmniOutliner suite
---
```

## Command: ungroup

**Description:** Decrease the outline level of all children of a row, moving them left one step.

### Direct Parameter
- **Description:** The rows to ungroup.
- **Types:** row, row
<a name="hoist"></a>
```yaml
---
type: command
name: hoist
suite: OmniOutliner suite
---
```

## Command: hoist

**Description:** Hide all rows in the outline, except for the descendants of the row passed to this command.

### Direct Parameter
- **Description:** The row or rows to focus on.
- **Types:** row, row
<a name="unhoist"></a>
```yaml
---
type: command
name: unhoist
suite: OmniOutliner suite
---
```

## Command: unhoist

**Description:** Show rows hidden in the last hoist operation on a document.

### Direct Parameter
- **Description:** The document to unhoist.
- **Types:** document, document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| unhoisting all | Reverse just the last Hoist operation on the outline, or show items hidden by all previous Hoist operations. | boolean | Yes |

<a name="import"></a>
```yaml
---
type: command
name: import
suite: OmniOutliner suite
---
```

## Command: import

**Description:** Imports a file, as rows, to a specified location. Returns the list of imported rows.

### Direct Parameter
- **Description:** The file to import.
- **Types:** file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | Where to place the imported rows. | location specifier | No |

### Result
- **Types:** row
<a name="export"></a>
```yaml
---
type: command
name: export
suite: OmniOutliner suite
---
```

## Command: export

**Description:** Exports the document to the specified location and file type. Unlike the "save" command, this will never set the name of the document or change its modified flag.

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | Where to place the exported document. | file | No |
| as | The name of a writable file type to use when writing the document. Defaults to the appropriate type for the path extension on the export destination. | text | Yes |

<a name="indent"></a>
```yaml
---
type: command
name: indent
suite: OmniOutliner suite
---
```

## Command: indent

**Description:** Indent one or more items.

### Direct Parameter
- **Description:** the item(s) to outdent
- **Types:** specifier, specifier
<a name="outdent"></a>
```yaml
---
type: command
name: outdent
suite: OmniOutliner suite
---
```

## Command: outdent

**Description:** Outdent one or more items.

### Direct Parameter
- **Description:** the item(s) to outdent
- **Types:** specifier, specifier
<a name="open_with_results"></a>
```yaml
---
type: command
name: open with results
suite: OmniOutliner suite
---
```

## Command: open with results

**Description:** Opens the specified files, returning references to them, or missing value for files that couldn't be opened.

### Direct Parameter
- **Description:** The file(s) to be opened.
- **Types:** file, file
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| skip errors | If set, the result array will not contain any 'missing value' entries.  You can use this when you don't care to know about which inputs failed to be opened. | boolean | Yes |
| with properties | A property record which can be used to pass extra information to the command. | record | Yes |

### Result
- **Description:** The opened document(s).
- **Types:** document, document
<a name="organize"></a>
```yaml
---
type: command
name: organize
suite: OmniOutliner suite
---
```

## Command: organize

**Description:** Builds a tree of rows based on the values in the specified columns.

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| by | What columns to consider when organizing the rows. | item | No |
| under | The row or document under which to place the organized rows. | row | No |
| prune | If set, any previously existing groups that end up empty after the reorganization will be deleted. | boolean | Yes |

### Result
- **Types:** item
<a name="redo"></a>
```yaml
---
type: command
name: redo
suite: OmniOutliner suite
---
```

## Command: redo

**Description:** Redoes the most recent undo operation.

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
<a name="set_parameter"></a>
```yaml
---
type: command
name: set parameter
suite: OmniOutliner suite
---
```

## Command: set parameter

**Description:** Sets the XPath expression for a parameter.  Note that to set a string constant you must quote the string.  For example "foo" means "element foo" but "'foo'" means "constant string 'foo'"

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The value of the parameter | text | No |
| named | The name of the parameter | text | No |

<a name="undo"></a>
```yaml
---
type: command
name: undo
suite: OmniOutliner suite
---
```

## Command: undo

**Description:** Undoes the most recent change.

### Direct Parameter
- **Description:** the object for the command
- **Types:** specifier
<a name="evaluate_javascript"></a>
```yaml
---
type: command
name: evaluate javascript
suite: OmniOutliner suite
---
```

## Command: evaluate javascript

**Description:** Evaluate the passed in text as JavaScript and return the result (if any).

### Direct Parameter
- **Description:** the script to evaluate
- **Types:** text
### Result
- **Types:** any, any
<a name="select"></a>
```yaml
---
type: command
name: select
suite: OmniOutliner suite
---
```

## Command: select

**Description:** Select one or more objects.

### Direct Parameter
- **Description:** the object(s) to select.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| extending | Whether the selection is replaced or extended. | boolean | Yes |

<a name="pbcopy"></a>
```yaml
---
type: command
name: pbcopy
suite: OmniOutliner suite
---
```

## Command: pbcopy

**Description:** Copies one or more nodes to the pasteboard.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| items | The items to copy the the pasteboard. | specifier, specifier | No |
| as | The list of type identifiers to use when copying the trees.  If omitted, all writable pasteboard types are used. | text, text | Yes |
| to | The name of the pasteboard to copy to. | text | Yes |

<a name="pbpaste"></a>
```yaml
---
type: command
name: pbpaste
suite: OmniOutliner suite
---
```

## Command: pbpaste

**Description:** Pastes nodes from the pasteboard.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | The location at which to paste the nodes. | location specifier | No |
| from | The name of the pasteboard to paste from. | text | Yes |

<a name="pbsave"></a>
```yaml
---
type: command
name: pbsave
suite: OmniOutliner suite
---
```

## Command: pbsave

**Description:** Saves data from the pasteboard to a file.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file to save to. | file | No |
| as | The pasteboard type to save. | text | No |
| from | The name of the pasteboard to save from. | text | Yes |

<a name="document_type"></a>
```yaml
---
type: class
name: document type
suite: OmniOutliner suite
---
```

## Class: document type

**Description:** A description of a document type

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| UTI | The Uniform Type Identifier for this document type | text | read/write |
| display name | A user-presentable display name for this document type | text | read/write |
| file extensions | File extensions for this document type | text | read/write |

<a name="readable_document_type"></a>
```yaml
---
type: class
name: readable document type
suite: OmniOutliner suite
---
```

## Class: readable document type

**Description:** A description of a document type

**Inherits:** document type

<a name="writable_document_type"></a>
```yaml
---
type: class
name: writable document type
suite: OmniOutliner suite
---
```

## Class: writable document type

**Description:** A description of a document type

**Inherits:** document type

<a name="row"></a>
```yaml
---
type: class
name: row
suite: OmniOutliner suite
---
```

## Class: row

**Description:** The flattened list of descendent rows underneath a document or another row.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| children are sections | Whether the row's children are treated as separate sections. | boolean | read/write |
| document | The document containing the row. | document | r |
| expanded | Whether the row's subtopics are visible. | boolean | read/write |
| has subtopics | Whether the row has any subtopics. | boolean | r |
| id | An identifier for the row that is unique within the document | text | r |
| name | The name of the row (just a plain string version of the topic). | text | r |
| index | The index of the row among its siblings | integer | read/write |
| level | How 'deep' this item is. Top-level rows are level 1, subtopics of those rows are level 2, and so on. | integer | r |
| note | Contents of the note column. | rich text | read/write |
| note cell | The cell for the note column in the row | cell | r |
| note expanded | Whether inline note is currently displayed | boolean | read/write |
| parent | The row that contains this row | row | r |
| selected | This is true if the row is selected.  Note that attempts to set this while the row is not visible (collapsed parent, hoisted root isn't an ancestor, etc.) will silently do nothing. | boolean | read/write |
| state | The state of the check box for this row. | checkbox state | read/write |
| style | The style of the row. | style | read/write |
| topic | Contents of the outline column. | rich text | read/write |
| topic cell | The cell for the topic column in the row | cell | r |
| visible | Whether this row is in the outline view. It must be a descendent of the current root item taking hoisting into account, with no collapsed ancestors below the current root. Hoisted rows are visible in the outline and so are considered visible. | boolean | r |

### Elements
- **Type:** ancestor
- **Type:** cell
- **Type:** row
- **Type:** child
- **Type:** conduit setting domain
- **Type:** following sibling
- **Type:** leaf
- **Type:** paragraph
- **Type:** path component
- **Type:** preceding sibling
- **Type:** section
- **Type:** selected row
### Responds To
- **Command:** expandAll
- **Command:** collapseAll
- **Command:** expel ancestors
- **Command:** expel descendants
- **Command:** import
- **Command:** indent
- **Command:** organize
- **Command:** outdent
- **Command:** select
- **Command:** group
- **Command:** ungroup
- **Command:** hoist
- **Command:** add
- **Command:** remove
- **Command:** pbcopy
- **Command:** pbpaste
<a name="child"></a>
```yaml
---
type: class
name: child
suite: OmniOutliner suite
---
```

## Class: child

**Description:** For a document, the top level rows. For a row, the rows one level below this one.

**Inherits:** row

<a name="ancestor"></a>
```yaml
---
type: class
name: ancestor
suite: OmniOutliner suite
---
```

## Class: ancestor

**Description:** The rows that this row is contained by, from the top level on down.

**Inherits:** row

<a name="section"></a>
```yaml
---
type: class
name: section
suite: OmniOutliner suite
---
```

## Class: section

**Description:** The sections underneath the document or row.  Note that a row is not a section of itself, so if you access this on a single row, an empty list will be returned.

**Inherits:** row

<a name="selected_row"></a>
```yaml
---
type: class
name: selected row
suite: OmniOutliner suite
---
```

## Class: selected row

**Description:** A selected row within a document

**Inherits:** row

<a name="leaf"></a>
```yaml
---
type: class
name: leaf
suite: OmniOutliner suite
---
```

## Class: leaf

**Description:** The leaf rows underneath a document or row.  Note that a row is not its own leaf, so if you access this on a single row with no children, that row will not be returned (use the command 'bottom rows' for that).

**Inherits:** row

<a name="following_sibling"></a>
```yaml
---
type: class
name: following sibling
suite: OmniOutliner suite
---
```

## Class: following sibling

**Description:** The row which follows this row.

**Inherits:** row

<a name="preceding_sibling"></a>
```yaml
---
type: class
name: preceding sibling
suite: OmniOutliner suite
---
```

## Class: preceding sibling

**Description:** The row which precedes this row.

**Inherits:** row

<a name="path_component"></a>
```yaml
---
type: class
name: path component
suite: OmniOutliner suite
---
```

## Class: path component

**Description:** A list of rows up to and including the given row.

**Inherits:** row

<a name="level_style"></a>
```yaml
---
type: class
name: level style
suite: OmniOutliner suite
---
```

## Class: level style

**Description:** A level styles in a document.

**Inherits:** style

<a name="cell"></a>
```yaml
---
type: class
name: cell
suite: OmniOutliner suite
---
```

## Class: cell

**Description:** The intersection of an item and a column. One value.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| column | Column that this cell is in | column | r |
| state | State of the cell.  This is only valid on checkbox columns. | checkbox state | read/write |
| id | The unique identifier of the cell within the containing row.  This identifier is the same as the identifier of the cell's column. | text | r |
| rich text | Text of the cell. This is only valid on text columns. | rich text | read/write |
| value | Contents of the cell, whatever the type. | text, date, number, enumeration, checkbox state, missing value | read/write |
| row | Row that this cell is in | row | r |
| name | The name of the cell.  This is the same as the name of the cell's column. | text | r |

### Responds To
- **Command:** replace
<a name="column"></a>
```yaml
---
type: class
name: column
suite: OmniOutliner suite
---
```

## Class: column

**Description:** An outline column.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| alignment | Default alignment for cells of column. | text alignment type | read/write |
| background color | The background color of the column | color | read/write |
| column style | The style of the column.  This is used as the default style for values in the column (but is overriden by any style attributes defined on rows) | style | read/write |
| document | The document containing the column. | document | r |
| column format | All aspects of the column's format. | column format | read/write |
| format string | The format string for formatted columns. Depends on the type of the column. | text | read/write |
| id | An identifier for the column that is unique within the document | text | r |
| index | The index of the column in the document. This includes hidden columns. | integer | read/write |
| name | The name of the column.  This is currently the same as the title, but in the future the title may be styled while the name will always be a plain string. | text | read/write |
| sort order | The sort order of the column | sort order type | read/write |
| summary type | This is the summary type of the column. | column summary type | read/write |
| title | The title of the column. | text | read/write |
| column type | This is the type of the column. | column type | read/write |
| width | The width of the column in pixels. | integer | read/write |
| visible | Whether the column is visible or not. | boolean | read/write |

### Elements
- **Type:** enumeration
### Responds To
- **Command:** move
<a name="selected_column"></a>
```yaml
---
type: class
name: selected column
suite: OmniOutliner suite
---
```

## Class: selected column

**Description:** The selected columns

**Inherits:** column

<a name="conduit_setting_domain"></a>
```yaml
---
type: class
name: conduit setting domain
suite: OmniOutliner suite
---
```

## Class: conduit setting domain

**Description:** A group of custom settings from one external source.  Note that conduit setting domains should only be referenced by 'id'.  The first time one is referenced it will be created.  Any other type of access (by index, every, etc.) will produce an error.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the domain.  These should typically be in the reverse-DNS style of bundle identifiers ("com.mycompany.myproduct"). | text | r |
| settings | Values must be strings or 'missing value' (removes value).  To set a single entry, concatenate the current value with the changes and then re-set it.  Concatenating an empty and non-empty record crashes AppleScript, so 'missing value' will be returned. | record | read/write |
| external id | Identifies the conduit externally to OmniOutliner. This might be a record identifier in an external database.  This will not get copied when duplicating the row, or if a 'save as' or 'save to' operation is performed instead of a normal 'save'. | text | read/write |
| container | The row or document containing this group of conduit settings. | item | r |

<a name="enumeration"></a>
```yaml
---
type: class
name: enumeration
suite: OmniOutliner suite
---
```

## Class: enumeration

**Description:** A pop-up menu item value

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | An identifier for the enumeration that is unique within the column. | text | r |
| index | The index of the enumeration member in the column. | integer | read/write |
| name | The name of the enumeration | text | read/write |

### Responds To
- **Command:** move
<a name="xsl_transform"></a>
```yaml
---
type: class
name: xsl transform
suite: OmniOutliner suite
---
```

## Class: xsl transform

**Description:** This class represents an available XSL transformation that may be applied when loading or saving documents

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| directory extension | The prefered file extension for file-system representations of wrapped file documents handled by this plugin | text | read/write |
| directory index file name | When writing a document with attachments, this specifies the name of the index file written inside the directory containing the transformed XML. | text | read/write |
| write attachments | When writing a document with attachments, this specifies whether the attachments will be written to the output location. | boolean | read/write |
| display name | The human readable name for the transform. | text | read/write |
| file extension | The prefered file extension for file-system representations of flat file documents handled by this plugin | text | read/write |
| id | A unique identifier for the transform to be used as the 'as' parameter of the 'save' command | text | r |
| is export | Returns true if the source format is a native format for OmniOutliner | boolean | r |
| is import | Returns true if the result format is a native format for OmniOutliner | boolean | r |
| parameter names | Names of all XSL parameters set on this transform | text | r |
| result format | A description of the data type produced by this transform.  For XML data types, this is the DTD public identifier. | text | read/write |
| source format | A description of the data type consumed by this transform.  For XML data types, this is the DTD public identifier. | text | read/write |
| stylesheet | The XSL source for the transform | text | read/write |

### Responds To
- **Command:** get parameter
- **Command:** set parameter
<a name="note_display_type"></a>
```yaml
---
type: enumeration
name: note display type
suite: OmniOutliner suite
---
```

## Enumeration: note display type

### Enumerators
| Name | Description |
|---|---|
| in line | None |
| out of line | None |

<a name="sort_order_type"></a>
```yaml
---
type: enumeration
name: sort order type
suite: OmniOutliner suite
---
```

## Enumeration: sort order type

### Enumerators
| Name | Description |
|---|---|
| ascending | None |
| descending | None |
| none | None |

<a name="checkbox_state"></a>
```yaml
---
type: enumeration
name: checkbox state
suite: OmniOutliner suite
---
```

## Enumeration: checkbox state

### Enumerators
| Name | Description |
|---|---|
| checked | None |
| unchecked | None |
| none | None |
| indeterminate | None |

<a name="column_type"></a>
```yaml
---
type: enumeration
name: column type
suite: OmniOutliner suite
---
```

## Enumeration: column type

### Enumerators
| Name | Description |
|---|---|
| styled text | None |
| checkbox | None |
| datetime | None |
| duration | None |
| popup | None |
| numeric | None |

<a name="column_summary_type"></a>
```yaml
---
type: enumeration
name: column summary type
suite: OmniOutliner suite
---
```

## Enumeration: column summary type

### Enumerators
| Name | Description |
|---|---|
| none | None |
| hidden | None |
| calculated | None |
| total | None |
| maximum | None |
| minimum | None |
| average | None |

<a name="text_alignment_type"></a>
```yaml
---
type: enumeration
name: text alignment type
suite: OmniOutliner suite
---
```

## Enumeration: text alignment type

### Enumerators
| Name | Description |
|---|---|
| center | None |
| justified | None |
| left | None |
| natural | None |
| right | None |

<a name="format_style"></a>
```yaml
---
type: enumeration
name: format style
suite: OmniOutliner suite
---
```

## Enumeration: format style

### Enumerators
| Name | Description |
|---|---|
| short style | None |
| medium style | None |
| long style | None |
| full style | None |

<a name="column_format"></a>
```yaml
---
type: record-type
name: column format
suite: OmniOutliner suite
---
```

## Record Type: column format

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| format | The ICU format string. | text | read/write |
| id | The identifier for built-in formats. | text, missing value | read/write |
| calendar | The calendar to use for date formats. | text, missing value | read/write |
| locale | The locale identifier (such as "en_US" or "ja_JP") for formats. | text, missing value | read/write |
| timezone | The time zone to use for date formats. | text, missing value | read/write |
| date style | The style of date format to use, based off the user's preference. | format style, format style, missing value | read/write |
| time style | The style of time format to use, based off the user's preference. | format style, format style, missing value | read/write |
| currency | The ISO currency identifier (such as "USD" or "JPY") for columns with a currency format. Must be used with an id of "currency". | text, missing value | read/write |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: OmniOutliner suite
---
```

## Class Extension: application

**Description:** The OmniOutliner application.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| build number | The build number of the application, for example 63.1 or 63. Major and minor versions are separated by a dot, so 63.10 comes after 63.1. | text | r |
| imported files should store compressed | Controls whether OmniOutliner will default imported files to being stored in a compressed format. | boolean | read/write |
| prompt on file format upgrade | Controls whether OmniOutliner will prompt the user when updating a older file format to a newer one. | boolean | read/write |

### Elements
- **Type:** preference
- **Type:** document type
- **Type:** readable document type
- **Type:** writable document type
- **Type:** xsl transform
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: OmniOutliner suite
---
```

## Class Extension: document

**Description:** An OmniOutliner document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| alternate color | The background color of every other row | color | read/write |
| background color | The background color of the document. | color | read/write |
| canRedo | Whether the document can redo the most recently undone command. | boolean | r |
| canUndo | Whether the document can undo the most recent command. | boolean | r |
| children are sections | This is always true for documents.  This is here to make it easier to deal with mixed lists of rows and documents. | boolean | r |
| column title style | The style of column titles. | style | read/write |
| editable | This lets you know whether the document is editable.  For example, the release notes document is not editable, so your script may want to avoid trying to edit it. | boolean | r |
| folded editing enabled | Whether folded editing of item and inline note text is enabled | boolean | read/write |
| has subtopics | Whether the document has any subtopics. | boolean | r |
| horizontal grid color | The color hairline dividers between rows. | color | read/write |
| id | An identifier unique to the document | text | r |
| note column | The column of the document that contains the notes for the rows | column | r |
| note display | Whether notes are displayed inline | note display type | read/write |
| save identifier | A string that changes each time the document is saved.  If the save identifier is disabled, then this returns 'missing value'. | text | r |
| save identifier enabled | Controls whether a save identifier will be emitted in the archived document each time the document is saved.  This is useful for external tools that need to quickly determine whether the document has changed without relying on the file modifictaion time ( | boolean | read/write |
| sorting postponed | Whether sorting is currently postponed for the document | boolean | read/write |
| status sort order | The sort order used for the status checkbox in the topic column | sort order type | read/write |
| status visible | Whether the status checkbox is visible in the outline column. | boolean | read/write |
| store compressed | Whether xml should be compressed when saved | boolean | read/write |
| style | The default style for the document. | style | read/write |
| title | This is the title of the document. | rich text | read/write |
| topic column | The column of the document that displays the hierarchy of rows | column | r |
| undo enabled | Controls whether undo is currently enabled in the document.  This should be used very carefully.  If it is set to 'false', all previously registered undo events will be removed and any further modifications to the document will not record undo operations. | boolean | read/write |
| vertical grid color | The color hairline dividers between columns. | color | read/write |
| visible | Whether the interface for the document is visible.  Note that miniaturized counts as visible.  Mostly this isn't useful to third parties right now. | boolean | r |
| writes wrapper | If set to true, this indicates that the document will write itself as a file wrapper (folder). | boolean | read/write |
| automatic level styles |  | boolean | read/write |
| topicColumnId | The topic column id for newly created documents. | text | read/write |
| noteColumnId | The topic column id for newly created documents. | text | read/write |

### Elements
- **Type:** selected column
- **Type:** section
- **Type:** selected row
- **Type:** child
- **Type:** column
- **Type:** row
- **Type:** leaf
- **Type:** level style
- **Type:** named style
### Responds To
- **Command:** undo
- **Command:** redo
- **Command:** select
- **Command:** add
- **Command:** remove
- **Command:** expandAll
- **Command:** collapseAll
- **Command:** group
- **Command:** ungroup
- **Command:** hoist
- **Command:** unhoist
- **Command:** pbcopy
- **Command:** pbpaste
- **Command:** export
## OmniStyle Scripting

**Description:** Scripting for Omni's style framework.

<a name="style"></a>
```yaml
---
type: class
name: style
suite: OmniStyle Scripting
---
```

## Class: style

**Description:** A style object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| container | The object owning the style. | item | r |
| font | The name of the font of the style. | text | read/write |

### Elements
- **Type:** named style
- **Type:** attribute
### Responds To
- **Command:** add
- **Command:** remove
<a name="attribute"></a>
```yaml
---
type: class
name: attribute
suite: OmniStyle Scripting
---
```

## Class: attribute

**Description:** An attribute of a style.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the attribute. | text | r |
| style | The style to which the attribute refers. | style | read/write |
| has local value | If true, the containing style defines a local value for this attribute. | boolean | r |
| defining style | The style responsible for the effective value in this attributes's style.  This processes the local values, inherited styles and cascade chain. | style | r |
| value | The value of the attribute in its style. | generic color, color, text, file, point, real, real, integer, boolean, point, missing value | read/write |
| default value | The default value of the attribute in its style. | generic color, color, text, file, point, real, real, integer, boolean, point, missing value | read/write |

### Responds To
- **Command:** clear
<a name="named_style"></a>
```yaml
---
type: class
name: named style
suite: OmniStyle Scripting
---
```

## Class: named style

**Description:** A named style object.

**Inherits:** style

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | An identifier for the named style that is unique within its document.  Currently this identifier is not persistent between two different sessions of editing the document. | text | r |
| name | The name of the style.  Must be unique within the containing document. | text | read/write |

<a name="point"></a>
```yaml
---
type: record-type
name: point
suite: OmniStyle Scripting
---
```

## Record Type: point

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| x | The x coordinate of the point. | real | read/write |
| y | The y coordinate of the point. | real | read/write |

<a name="generic_color"></a>
```yaml
---
type: record-type
name: generic color
suite: OmniStyle Scripting
---
```

## Record Type: generic color

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| r | If the color is in a RGB color space, this is the calibrated floating point red component, from zero to one. | real | read/write |
| g | If the color is in a RGB color space, this is the calibrated floating point green component, from zero to one. | real | read/write |
| b | If the color is in a RGB color space, this is the calibrated floating point blue component, from zero to one. | real | read/write |
| w | If the color is in a White color space, this is the calibrated floating point white component, from zero to one, with zero being totally black and one being totally white. | real | read/write |
| c | If the color is in a CMYK color space, this is the device-specific floating point cyan component, from zero to one.  There is currently no support for calibrated CYMK color spaces. | real | read/write |
| y | If the color is in a CMYK color space, this is the device-specific floating point yellow component, from zero to one.  There is currently no support for calibrated CYMK color spaces. | real | read/write |
| m | If the color is in a CMYK color space, this is the device-specific floating point magenta component, from zero to one.  There is currently no support for calibrated CYMK color spaces. | real | read/write |
| k | If the color is in a CMYK color space, this is the device-specific floating point black component, from zero to one.  There is currently no support for calibrated CYMK color spaces. | real | read/write |
| h | If the color is in a HSV color space, this is the calibrated floating point hue component, from zero to one. | real | read/write |
| s | If the color is in a HSV color space, this is the calibrated floating point saturation component, from zero to one. | real | read/write |
| v | If the color is in a HSV color space, this is the calibrated floating point value component, from zero to one. | real | read/write |
| a | The opacity or alpha of the color as a floating point number from zero to one with zero being totally transparent and one being totally opaque. | real | read/write |
| catalog | If the color is in a catalog color space, this is the name of the catalog. | text | read/write |
| name | If the color is in a catalog color space, this is the name of color with in the catalog. | text | read/write |
| png | If the color is in a pattern color space, this is PNG data for the image representing the pattern. | PNG data | read/write |
| tiff | If the color is in a pattern color space, this is TIFF data for the image representing the pattern. | TIFF data | read/write |
| archive | If the color cannot be represented in any other format, a binary archive is placed in this property. | archive data | read/write |

<a name="color"></a>
```yaml
---
type: value-type
name: color
suite: OmniStyle Scripting
---
```

## Value Type: color

<a name="tiff_data"></a>
```yaml
---
type: value-type
name: TIFF data
suite: OmniStyle Scripting
---
```

## Value Type: TIFF data

<a name="png_data"></a>
```yaml
---
type: value-type
name: PNG data
suite: OmniStyle Scripting
---
```

## Value Type: PNG data

<a name="archive_data"></a>
```yaml
---
type: value-type
name: archive data
suite: OmniStyle Scripting
---
```

## Value Type: archive data

## Omni Text Suite

**Description:** A set of basic classes for text processing.

<a name="insert"></a>
```yaml
---
type: command
name: insert
suite: Omni Text Suite
---
```

## Command: insert

**Description:** Insert text in the middle of an existing blob of text.

### Direct Parameter
- **Description:** the string to insert.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | Where to insert the text. | location specifier | No |
| using | The style to use when inserting the text.  If missing, the default style for this text will be used. | style | Yes |

<a name="clear"></a>
```yaml
---
type: command
name: clear
suite: Omni Text Suite
---
```

## Command: clear

**Description:** Clears a locally set value for a style attribute.

### Direct Parameter
- **Description:** The attributes to clear.
- **Types:** attribute, attribute
<a name="rich_text"></a>
```yaml
---
type: class
name: rich text
suite: Omni Text Suite
---
```

## Class: rich text

**Description:** Rich (styled) text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| text | The plain text contents of the rich text. | text | read/write |
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |
| style | The style of the text. | style | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
- **Type:** file attachment
### Responds To
- **Command:** delete
- **Command:** insert
- **Command:** duplicate
<a name="character"></a>
```yaml
---
type: class
name: character
suite: Omni Text Suite
---
```

## Class: character

**Description:** This subdivides the text into characters.

**Inherits:** rich text

<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: Omni Text Suite
---
```

## Class: paragraph

**Description:** This subdivides the text into paragraphs.

**Inherits:** rich text

<a name="word"></a>
```yaml
---
type: class
name: word
suite: Omni Text Suite
---
```

## Class: word

**Description:** This subdivides the text into words.

**Inherits:** rich text

<a name="attribute_run"></a>
```yaml
---
type: class
name: attribute run
suite: Omni Text Suite
---
```

## Class: attribute run

**Description:** This subdivides the text into chunks that all have the same attributes.

**Inherits:** rich text

<a name="attachment"></a>
```yaml
---
type: class
name: attachment
suite: Omni Text Suite
---
```

## Class: attachment

**Description:** Represents an inline text attachment.

**Inherits:** rich text

<a name="file_attachment"></a>
```yaml
---
type: class
name: file attachment
suite: Omni Text Suite
---
```

## Class: file attachment

**Description:** A text attachment refering to a plain file.

**Inherits:** attachment

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The path to the file for the attachment, if the attachment resides outside the document. | file | r |
| embedded | If true, the attached file will reside inside the document on the next save. | boolean | r |

### Responds To
- **Command:** save
## Extended Text Suite

**Description:** Extended functionality for text.

<a name="bold"></a>
```yaml
---
type: command
name: bold
suite: Extended Text Suite
---
```

## Command: bold

**Description:** Bold some text

### Direct Parameter
- **Types:** rich text
<a name="italicize"></a>
```yaml
---
type: command
name: italicize
suite: Extended Text Suite
---
```

## Command: italicize

**Description:** Italicize some text

### Direct Parameter
- **Types:** rich text
<a name="replace"></a>
```yaml
---
type: command
name: replace
suite: Extended Text Suite
---
```

## Command: replace

### Direct Parameter
- **Types:** rich text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| matching regular expression | Regular expression to find | text | Yes |
| replacement | Replacement string | text | No |
| string | String to find | text | Yes |

<a name="unbold"></a>
```yaml
---
type: command
name: unbold
suite: Extended Text Suite
---
```

## Command: unbold

**Description:** Unbold some text

### Direct Parameter
- **Types:** rich text
<a name="underline"></a>
```yaml
---
type: command
name: underline
suite: Extended Text Suite
---
```

## Command: underline

**Description:** Underline some text

### Direct Parameter
- **Types:** rich text
<a name="unitalicize"></a>
```yaml
---
type: command
name: unitalicize
suite: Extended Text Suite
---
```

## Command: unitalicize

**Description:** Unitalicize some text

### Direct Parameter
- **Types:** rich text
<a name="ununderline"></a>
```yaml
---
type: command
name: ununderline
suite: Extended Text Suite
---
```

## Command: ununderline

**Description:** Ununderline some text

### Direct Parameter
- **Types:** rich text
<a name="textalignment"></a>
```yaml
---
type: enumeration
name: TextAlignment
suite: Extended Text Suite
---
```

## Enumeration: TextAlignment

### Enumerators
| Name | Description |
|---|---|
| left | None |
| right | None |
| center | None |
| justified | None |
| natural | None |

<a name="rich_text"></a>
```yaml
---
type: class-extension
name: rich text
suite: Extended Text Suite
---
```

## Class Extension: rich text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| baseline offset | Number of pixels shifted above or below the normal baseline. | real | read/write |
| underlined | Is the first character underlined? | boolean | read/write |
| superscript | The superscript level of the text. | integer | read/write |
| alignment | Alignment of the text. | TextAlignment | read/write |

### Responds To
- **Command:** bold
- **Command:** italicize
- **Command:** replace
- **Command:** unbold
- **Command:** underline
- **Command:** unitalicize
- **Command:** ununderline
## OmniFoundation Scripting

**Description:** OmniFoundation scripting support.

<a name="add"></a>
```yaml
---
type: command
name: add
suite: OmniFoundation Scripting
---
```

## Command: add

**Description:** Add the given object(s) to the container.

### Direct Parameter
- **Description:** the object(s) to add.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The container to which to add the object. | specifier, location specifier | No |

<a name="remove"></a>
```yaml
---
type: command
name: remove
suite: OmniFoundation Scripting
---
```

## Command: remove

**Description:** Remove the given object(s) from the container.

### Direct Parameter
- **Description:** the object(s) to remove.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The container from which to remove the object. | specifier | No |

<a name="preference"></a>
```yaml
---
type: class
name: preference
suite: OmniFoundation Scripting
---
```

## Class: preference

**Description:** Application preference

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the preference. | text | r |
| value | The current value of the preference. | text, real, integer, boolean, missing value | read/write |
| default value | The default value of the preference. | text, real, integer, boolean, missing value | read/write |

