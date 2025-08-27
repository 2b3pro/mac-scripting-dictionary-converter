# OmniFocus Terminology: AppleScript/JSX

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
### OmniFocus suite
#### Commands
- [archive](#archive)
- [resettextdump](#resettextdump)
- [textdump](#textdump)
- [compact](#compact)
- [complete](#complete)
- [evaluate javascript](#evaluate_javascript)
- [mark complete](#mark_complete)
- [mark incomplete](#mark_incomplete)
- [mark dropped](#mark_dropped)
- [parse tasks into](#parse_tasks_into)
- [undo](#undo)
- [redo](#redo)
- [synchronize](#synchronize)
- [import into](#import_into)
- [summarize clipped text](#summarize_clipped_text)
#### Classs
- [document window](#document_window)
- [quick entry tree](#quick_entry_tree)
- [setting](#setting)
- [focus sections](#focus_sections)
- [section](#section)
- [folder](#folder)
- [tag](#tag)
- [deprecated context](#deprecated_context)
- [project](#project)
- [task](#task)
- [forecast sidebar tree](#forecast_sidebar_tree)
- [forecast day](#forecast_day)
- [available task](#available_task)
- [remaining task](#remaining_task)
- [inbox task](#inbox_task)
- [flattened task](#flattened_task)
- [flattened project](#flattened_project)
- [flattened folder](#flattened_folder)
- [flattened tag](#flattened_tag)
- [sidebar tree](#sidebar_tree)
- [content tree](#content_tree)
- [inbox tree](#inbox_tree)
- [library tree](#library_tree)
- [perspective](#perspective)
- [builtin perspective](#builtin_perspective)
- [custom perspective](#custom_perspective)
#### Enumerations
- [project status](#project_status)
- [interval unit](#interval_unit)
- [repetition method](#repetition_method)
- [location trigger](#location_trigger)
- [sidebar tab](#sidebar_tab)
#### Record Types
- [repetition interval](#repetition_interval)
- [repetition rule](#repetition_rule)
- [location information](#location_information)
- [completion match](#completion_match)
- [summarized text result](#summarized_text_result)
#### Class Extensions
- [application](#application)
- [document](#document)
### Omni Tree Suite
#### Commands
- [pbcopy](#pbcopy)
- [pbpaste](#pbpaste)
- [pbsave](#pbsave)
#### Classs
- [tree](#tree)
- [descendant tree](#descendant_tree)
- [ancestor tree](#ancestor_tree)
- [leaf](#leaf)
- [following sibling](#following_sibling)
- [preceding sibling](#preceding_sibling)
- [selected tree](#selected_tree)
#### Record Types
- [pasteboard type](#pasteboard_type)
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
| using cache | Should opening the document use any existing data cache or rebuild the cache from the document.  Defaults to true. | boolean | Yes |
| upgrade in place | If the document needs to be upgraded from an older file format version and this is set, the upgrade will be attempted in place without any alert or backup prior to upgrade.  Defaults to false. | boolean | Yes |
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
| compression | Should the file be written with data compression enabled?  Defaults to true. | boolean | Yes |

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
- **Types:** specifier
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
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new copy or copies. | location specifier | Yes |
| with properties | Properties to set in the new copy or copies right away. | record | Yes |

### Result
- **Description:** the duplicated object(s)
- **Types:** specifier, specifier
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

### Result
- **Description:** the moved object(s)
- **Types:** specifier
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
| target file | the file to save the results in | file | read/write |
| show preview | open the results in Preview instead of printing | boolean | read/write |

## OmniFocus suite

**Description:** AppleScript commands and classes specific to OmniFocus.

<a name="archive"></a>
```yaml
---
type: command
name: archive
suite: OmniFocus suite
---
```

## Command: archive

**Description:** Write an backup archive of the document.

### Direct Parameter
- **Description:** The document to archive.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file in which to archive the document. | file | No |
| compression | Should the archive be written with data compression enabled?  Defaults to true. | boolean | Yes |
| summaries | Should the archive be written with summaries enabled?  Defaults to false. | boolean | Yes |
| using cache | Should the document generate new XML from its data cache?  Defaults to false unless summaries are enabled. | boolean | Yes |

### Result
- **Description:** The archived document.
- **Types:** specifier
<a name="resettextdump"></a>
```yaml
---
type: command
name: resettextdump
suite: OmniFocus suite
---
```

## Command: resettextdump

**Description:** Reset internal identifier state for text dumps; used for testing.

### Direct Parameter
- **Description:** The document to reset.
- **Types:** specifier
<a name="textdump"></a>
```yaml
---
type: command
name: textdump
suite: OmniFocus suite
---
```

## Command: textdump

**Description:** Write an text based dump of the document; used for testing.

### Direct Parameter
- **Description:** The document to dump.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file in which to dump the document. | file | No |
| summaries | Should the dump be written with summaries enabled?  Defaults to false. | boolean | Yes |
| dates | Should the dump be written with creation and modification dates?  Defaults to false. | boolean | Yes |

### Result
- **Description:** The dumped document.
- **Types:** specifier
<a name="compact"></a>
```yaml
---
type: command
name: compact
suite: OmniFocus suite
---
```

## Command: compact

**Description:** Hides completed tasks and processes any inbox items that have the necessary information into projects and tasks.

### Direct Parameter
- **Description:** The document to compact.
- **Types:** specifier
<a name="complete"></a>
```yaml
---
type: command
name: complete
suite: OmniFocus suite
---
```

## Command: complete

**Description:** Generate a list of completions given a string.

### Direct Parameter
- **Description:** The string to complete from.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as | The class object to complete against.  'folder', 'project', and 'tag' are supported types. | type | No |
| span class | The XML class name to specify on <span> elements in the result XML elements.  Defaults to "match". | text | Yes |
| maximum matches | The maximum number of matches to return.  Zero or negative values indicate an unlimited number of matches.  Defaults to unlimited. | integer | Yes |

### Result
- **Description:** The matches.
- **Types:** completion match
<a name="evaluate_javascript"></a>
```yaml
---
type: command
name: evaluate javascript
suite: OmniFocus suite
---
```

## Command: evaluate javascript

**Description:** Evaluate the passed in text as JavaScript and return the result (if any).

### Direct Parameter
- **Description:** the script to evaluate
- **Types:** text
### Result
- **Types:** any, any
<a name="mark_complete"></a>
```yaml
---
type: command
name: mark complete
suite: OmniFocus suite
---
```

## Command: mark complete

**Description:** Mark one or more projects or tasks complete.

### Direct Parameter
- **Description:** The project, task, or list of projects and tasks to mark complete.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| completion date | The date to use when marking the project complete. | date | Yes |

### Result
- **Description:** The projects or tasks which were marked complete. For repeating projects or tasks, the a completed clone is created, and the current instance is configured for the next repetition.
- **Types:** specifier, specifier
<a name="mark_incomplete"></a>
```yaml
---
type: command
name: mark incomplete
suite: OmniFocus suite
---
```

## Command: mark incomplete

**Description:** Mark one or more projects or tasks incomplete.

### Direct Parameter
- **Description:** The project, task, or list of projects and tasks to mark incomplete.
- **Types:** specifier, specifier
<a name="mark_dropped"></a>
```yaml
---
type: command
name: mark dropped
suite: OmniFocus suite
---
```

## Command: mark dropped

**Description:** Mark one or more projects or tasks as dropped.

### Direct Parameter
- **Description:** The project, task, or list of projects and tasks to mark dropped.
- **Types:** specifier, specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| dropped date | The date to use when marking the project dropped. | date | Yes |

### Result
- **Description:** The projects or tasks which were marked dropped. For repeating projects or tasks, the a dropped clone is created, and the current instance is configured for the next repetition.
- **Types:** specifier, specifier
<a name="parse_tasks_into"></a>
```yaml
---
type: command
name: parse tasks into
suite: OmniFocus suite
---
```

## Command: parse tasks into

**Description:** Converts a textual representation of tasks into tasks.

### Direct Parameter
- **Description:** The document to parse tasks into.
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with transport text | The text to parse into tasks. | text | No |
| as single task | If true, the entire text will only generate one task instead of being split up into multiple tasks. | boolean | Yes |

### Result
- **Description:** The parsed tasks.
- **Types:** task
<a name="undo"></a>
```yaml
---
type: command
name: undo
suite: OmniFocus suite
---
```

## Command: undo

**Description:** Undo the last command.

### Direct Parameter
- **Description:** The document with the command to be undone.
- **Types:** specifier
<a name="redo"></a>
```yaml
---
type: command
name: redo
suite: OmniFocus suite
---
```

## Command: redo

**Description:** Redo the last undone command.

### Direct Parameter
- **Description:** The document with the command to be redone.
- **Types:** specifier
<a name="synchronize"></a>
```yaml
---
type: command
name: synchronize
suite: OmniFocus suite
---
```

## Command: synchronize

**Description:** Synchronizes with the shared OmniFocus sync database.

### Direct Parameter
- **Description:** The document to synchronize with the sync database defined in Sync Preferences.  (Note:  synchronization is only allowed with the default document.)
- **Types:** specifier
<a name="import_into"></a>
```yaml
---
type: command
name: import into
suite: OmniFocus suite
---
```

## Command: import into

**Description:** Imports a file into an existing OmniFocus document.

### Direct Parameter
- **Description:** The document to import into
- **Types:** document
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The file to import. | file | No |
| at | A section-relative location describing where to place the imported folders and projects. | location specifier | Yes |
| with tags at | Where to place the imported tags. | location specifier | Yes |

<a name="summarize_clipped_text"></a>
```yaml
---
type: command
name: summarize clipped text
suite: OmniFocus suite
---
```

## Command: summarize clipped text

**Description:** Summarize clipped text into a form suitable for a task title.

### Direct Parameter
- **Description:** The text to summarize.
- **Types:** text
### Result
- **Description:** The summarized text.
- **Types:** summarized text result
<a name="document_window"></a>
```yaml
---
type: class
name: document window
suite: OmniFocus suite
---
```

## Class: document window

**Description:** A window of an OmniFocus document.

**Inherits:** window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| search term | The search term in the toolbar.  If there is no search toolbar item, this will return missing value instead of an empty string and setting it will cause an error. | text | read/write |
| selected sidebar tab | The selected tab in the sidebar. | sidebar tab, perspective | read/write |
| sidebar | The tree of objects in the window sidebar. | sidebar tree, forecast sidebar tree | r |
| content | The tree of objects in the main window content. | content tree | r |
| perspective name | The name of a perspective. | text | read/write |
| focus | A list of the projects and folders forming the project focus of this document window. | item, focus sections, any | read/write |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="quick_entry_tree"></a>
```yaml
---
type: class
name: quick entry tree
suite: OmniFocus suite
---
```

## Class: quick entry tree

**Description:** The Quick Entry panel.

**Inherits:** tree

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| visible | Whether the quick entry panel is currently visible. | boolean | r |

### Elements
- **Type:** folder
- **Type:** project
- **Type:** tag
- **Type:** deprecated context
- **Type:** inbox task
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="setting"></a>
```yaml
---
type: class
name: setting
suite: OmniFocus suite
---
```

## Class: setting

**Description:** Document setting

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the setting. | text | r |
| value | The current value of the setting. | text, real, integer, boolean, missing value | read/write |
| default value | The default value of the setting. | text, real, integer, boolean, missing value | read/write |

<a name="focus_sections"></a>
```yaml
---
type: class
name: focus sections
suite: OmniFocus suite
---
```

## Class: focus sections

**Description:** The current focus of a document window.

### Elements
- **Type:** item
<a name="section"></a>
```yaml
---
type: class
name: section
suite: OmniFocus suite
---
```

## Class: section

**Description:** A portion of a folder or document; either a project or a folder.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the project or folder. | text | r |
| name | The name of the project or folder. | text | read/write |

<a name="folder"></a>
```yaml
---
type: class
name: folder
suite: OmniFocus suite
---
```

## Class: folder

**Description:** A group of projects and sub-folders representing an area of responsibility.

**Inherits:** section

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the folder. | text | r |
| name | The name of the folder. | text | read/write |
| note | The note of the folder. | rich text | read/write |
| hidden | Set if the folder is currently hidden. | boolean | read/write |
| effectively hidden | Set if the folder is currently hidden or any of its container folders are hidden. | boolean | r |
| creation date | When the folder was created. | date | r |
| modification date | When the folder was last modified. | date | r |
| container | The containing folder or document. | document, quick entry tree, folder | r |
| containing document | The containing document or quick entry tree of the object. | document, quick entry tree | r |

### Elements
- **Type:** section
- **Type:** folder
- **Type:** project
- **Type:** flattened project
- **Type:** flattened folder
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
<a name="tag"></a>
```yaml
---
type: class
name: tag
suite: OmniFocus suite
---
```

## Class: tag

**Description:** A tag.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the tag. | text | read/write |
| name | The name of the tag. | text | read/write |
| note | The note of the tag. | rich text | read/write |
| allows next action | If false, tasks associated with this tag will be skipped when determining the next action for a project. | boolean | read/write |
| hidden | Set if the tag is currently hidden. | boolean | read/write |
| effectively hidden | Set if the tag is currently hidden or any of its container tags are hidden. | boolean | r |
| container | The containing tag. | tag | r |
| available task count | A count of the number of unblocked and incomplete tasks of this tag and all its active descendent tags. | integer | r |
| remaining task count | A count of the number of incomplete tasks of this tag and all its active descendent tags. | integer | r |
| containing document | The containing document or quick entry tree of the object. | document, quick entry tree | r |
| location | The physical location associated with the tag. | location information, missing value | read/write |

### Elements
- **Type:** tag
- **Type:** deprecated context
- **Type:** flattened tag
- **Type:** task
- **Type:** available task
- **Type:** remaining task
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
<a name="deprecated_context"></a>
```yaml
---
type: class
name: deprecated context
suite: OmniFocus suite
---
```

## Class: deprecated context

**Description:** Deprecated. Where you would look up a "context" by name, id, or index before, you can now use the term "tag". Where you would get or set the "context" property of a task before, you can now use "primary tag". You may also use the "add", "remove", and "move" commands to manage multiple ordered tags on a task now.

**Inherits:** tag

<a name="project"></a>
```yaml
---
type: class
name: project
suite: OmniFocus suite
---
```

## Class: project

**Description:** A project.

**Inherits:** section

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the project. | text | read/write |
| next task | The next actionable child of this project. | task, missing value | r |
| last review date | When the project was last reviewed. | date | read/write |
| next review date | When the project should next be reviewed. Setting this to missing value will set the review date based off the last review date and review interval. | date, missing value | read/write |
| review interval | The review interval for the project. | repetition interval | read/write |
| status | The status of the project. | project status | read/write |
| effective status | The effective status of the project. | project status | r |
| singleton action holder | True if the project contains singleton actions. | boolean | read/write |
| default singleton action holder | True if the project is the default holder of sington actions.  Only one project can have this flag set; setting it on a project will clear it on any other project having it.  Setting this to true will set 'singleton action holder' to true if not already so set. | boolean | read/write |
| container | The containing folder or document. | document, quick entry tree, folder | r |
| folder | The folder of the project, or missing value if it is contained directly by the document. | folder, missing value | r |
| id | The identifier of the project. | text | read/write |
| name | The name of the project. | text | read/write |
| note | The note of the project. | rich text | read/write |
| containing document | The containing document or quick entry tree of the object. | document, quick entry tree | r |
| primary tag | The project's first tag. Setting this will remove the current first tag on the project, if any and move or add the new tag as the first tag on the project. Setting this to missing value will remove the current first tag and leave any other remaining tags. | tag, missing value | read/write |
| completed by children | If true, complete when children are completed. | boolean | read/write |
| sequential | If true, any children are sequentially dependent. | boolean | read/write |
| flagged | True if flagged | boolean | read/write |
| blocked | True if the project has a project that must be completed prior to it being actionable. | boolean | r |
| creation date | When the project was created.  This can only be set when the object is still in the inserted state.  For objects created in the document, it can be passed with the creation properties.  For objects in a quick entry tree, it can be set until the quick entry panel is saved. | date | read/write |
| modification date | When the project was last modified. | date | r |
| defer date | When the project should become available for action. | date, missing value | read/write |
| effective defer date | When the project should become available for action (including inherited). | date, missing value | r |
| due date | When the project must be finished. | date, missing value | read/write |
| effective due date | When the project must be finished (including inherited). | date, missing value | r |
| should use floating time zone | When set, the due date and defer date properties will use floating time zones. (Note: if a Task has no due or defer dates assigned, this property will revert to the database’s default setting.) | boolean | read/write |
| completion date | The project's date of completion. This can only be modified on a completed project to backdate the completion date. | date, missing value | read/write |
| completed | True if the project is completed. Use the "mark complete" and "mark incomplete" commands to change a project's status. | boolean | r |
| effectively completed | True if the project is completed | boolean | r |
| dropped date | The date the project was dropped. This can only be modified on a dropped project to backdate the dropped date. | date, missing value | read/write |
| dropped | True if the project is dropped. Use the "mark dropped" and "mark incomplete" commands to change a project's status. | boolean | r |
| effectively dropped | True if the project is dropped | boolean | r |
| estimated minutes | The estimated time, in whole minutes, that this project will take to finish. | integer, missing value | read/write |
| repetition | The repetition interval of the project, or missing value if it does not repeat. This property is deprecated in favor of “repetition rule” and is here only for backwards compatibility with existing scripts. | repetition interval, missing value | read/write |
| repetition rule | The repetition rule for this project, or missing value if it does not repeat. | repetition rule, missing value | read/write |
| next defer date | The next defer date if this project repeats on a fixed schedule and it has a defer date. | date, missing value | r |
| next due date | The next due date if this project repeats on a fixed schedule and it has a due date. | date, missing value | r |
| number of tasks | The number of direct children of this project. | integer | r |
| number of available tasks | The number of available direct children of this project. | integer | r |
| number of completed tasks | The number of completed direct children of this project. | integer | r |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="task"></a>
```yaml
---
type: class
name: task
suite: OmniFocus suite
---
```

## Class: task

**Description:** A task. This might represent the root of a project, an action within a project or other action or an inbox item.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the task. | text | read/write |
| name | The name of the task. | text | read/write |
| note | The note of the task. | rich text | read/write |
| container | The containing task, project or document. | document, quick entry tree, project, task | r |
| containing project | The task's project, up however many levels of parent tasks.  Inbox tasks aren't considered contained by their provisionalliy assigned container, so if the task is actually an inbox task, this will be missing value. | project, missing value | r |
| parent task | The task holding this task.  If this is missing value, then this is a top level task -- either the root of a project or an inbox item. | task, missing value | r |
| containing document | The containing document or quick entry tree of the object. | document, quick entry tree | r |
| in inbox | Returns true if the task itself is an inbox task or if the task is contained by an inbox task. | boolean | r |
| primary tag | The task's first tag. Setting this will remove the current first tag on the task, if any and move or add the new tag as the first tag on the task. Setting this to missing value will remove the current first tag and leave any other remaining tags. | tag, missing value | read/write |
| completed by children | If true, complete when children are completed. | boolean | read/write |
| sequential | If true, any children are sequentially dependent. | boolean | read/write |
| flagged | True if flagged | boolean | read/write |
| next | If the task is the next task of its containing project, next is true. | boolean | r |
| blocked | True if the task has a task that must be completed prior to it being actionable. | boolean | r |
| creation date | When the task was created.  This can only be set when the object is still in the inserted state.  For objects created in the document, it can be passed with the creation properties.  For objects in a quick entry tree, it can be set until the quick entry panel is saved. | date | read/write |
| modification date | When the task was last modified. | date | r |
| defer date | When the task should become available for action. | date, missing value | read/write |
| effective defer date | When the task should become available for action (including inherited). | date, missing value | r |
| due date | When the task must be finished. | date, missing value | read/write |
| effective due date | When the task must be finished (including inherited). | date, missing value | r |
| should use floating time zone | When set, the due date and defer date properties will use floating time zones. (Note: if a Task has no due or defer dates assigned, this property will revert to the database’s default setting.) | boolean | read/write |
| completion date | The task's date of completion. This can only be modified on a completed task to backdate the completion date. | date, missing value | read/write |
| completed | True if the task is completed. Use the "mark complete" and "mark incomplete" commands to change a task's status. | boolean | r |
| effectively completed | True if the task is completed, or any of it's containing tasks or project are completed. | boolean | r |
| dropped date | The date the task was dropped. This can only be modified on a dropped task to backdate the dropped date. | date, missing value | read/write |
| dropped | True if the task is dropped. Use the "mark dropped" and "mark incomplete" commands to change a task's status. | boolean | r |
| effectively dropped | True if the task is dropped, or any of it's containing tasks or project are dropped. | boolean | r |
| estimated minutes | The estimated time, in whole minutes, that this task will take to finish. | integer, missing value | read/write |
| repetition | The repetition interval of the task, or missing value if it does not repeat. This property is deprecated in favor of “repetition rule” and is here only for backwards compatibility with existing scripts. | repetition interval, missing value | read/write |
| repetition rule | The repetition rule for this task, or missing value if it does not repeat. | repetition rule, missing value | read/write |
| next defer date | The next defer date if this task repeats on a fixed schedule and it has a defer date. | date, missing value | r |
| next due date | The next due date if this task repeats on a fixed schedule and it has a due date. | date, missing value | r |
| number of tasks | The number of direct children of this task. | integer | r |
| number of available tasks | The number of available direct children of this task. | integer | r |
| number of completed tasks | The number of completed direct children of this task. | integer | r |

### Elements
- **Type:** tag
- **Type:** task
- **Type:** flattened task
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="forecast_sidebar_tree"></a>
```yaml
---
type: class
name: forecast sidebar tree
suite: OmniFocus suite
---
```

## Class: forecast sidebar tree

**Description:** The sidebar tree used when the window's sidebar tab property is set to forecast tab.

**Inherits:** sidebar tree

### Elements
- **Type:** forecast day
<a name="forecast_day"></a>
```yaml
---
type: class
name: forecast day
suite: OmniFocus suite
---
```

## Class: forecast day

**Description:** A day in the forecast sidebar tree.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the task. | text | read/write |
| name | A display name for the forecast day. | text | read/write |
| empty | True if the forecast day has no content at all. Note that some content will not cause a badge to be shown in the sidebar, and some content is controlled by user preferences. | boolean | read/write |
| badge count | The count shown in the sidebar for this forecast day, or zero if there is no count shown. | integer | read/write |

<a name="available_task"></a>
```yaml
---
type: class
name: available task
suite: OmniFocus suite
---
```

## Class: available task

**Description:** A task that is available for action.  This is simply a filter on the existing tasks and should be considred a read-only element.  These cannot be created directly; instead create a normal task.

**Inherits:** task

<a name="remaining_task"></a>
```yaml
---
type: class
name: remaining task
suite: OmniFocus suite
---
```

## Class: remaining task

**Description:** A task that is not complete, though it may be blocked.  This is simply a filter on the existing tasks and should be considred a read-only element.  These cannot be created directly; instead create a normal task.

**Inherits:** task

<a name="inbox_task"></a>
```yaml
---
type: class
name: inbox task
suite: OmniFocus suite
---
```

## Class: inbox task

**Description:** A task that is in the document's inbox

**Inherits:** task

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| assigned container | Inbox tasks (those contained directly by the document) have a provisionally set container that is made final by the 'compact' command.  This allows you to set and get said container.  The container must be either a task (not in the inbox or contained by an inbox task), a project or 'missing value'. | item | read/write |

<a name="flattened_task"></a>
```yaml
---
type: class
name: flattened task
suite: OmniFocus suite
---
```

## Class: flattened task

**Description:** A flattened list of tasks under a task or document.

**Inherits:** task

<a name="flattened_project"></a>
```yaml
---
type: class
name: flattened project
suite: OmniFocus suite
---
```

## Class: flattened project

**Description:** A flattened list of projects under a folder or document.

**Inherits:** project

<a name="flattened_folder"></a>
```yaml
---
type: class
name: flattened folder
suite: OmniFocus suite
---
```

## Class: flattened folder

**Description:** A flattened list of folders in a document.

**Inherits:** folder

<a name="flattened_tag"></a>
```yaml
---
type: class
name: flattened tag
suite: OmniFocus suite
---
```

## Class: flattened tag

**Description:** A flattened list of tags in a document.

**Inherits:** tag

<a name="sidebar_tree"></a>
```yaml
---
type: class
name: sidebar tree
suite: OmniFocus suite
---
```

## Class: sidebar tree

**Description:** The tree of objects in the window sidebar.

**Inherits:** tree

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| available smart group identifiers | The list of possible smart group identifiers that can be set as the selected smart group identifier. | text | r |
| selected smart group identifier | The currently selected smart group identifier. | text, missing value | read/write |

<a name="content_tree"></a>
```yaml
---
type: class
name: content tree
suite: OmniFocus suite
---
```

## Class: content tree

**Description:** The tree of objects in the main window content.

**Inherits:** tree

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| available grouping identifiers | The list of possible identifiers that can be set as the selected grouping identifier. | text | r |
| selected grouping identifier | The currently selected grouping identifier, controlling how the results shown in the content area are grouped. | text | read/write |
| available sorting identifiers | The list of possible identifiers that can be set as the selected sorting identifier. | text | r |
| selected sorting identifier | The currently selected sorting identifier, controlling how the results shown in the content area are ordered. | text | read/write |
| available task state filter identifiers | The list of possible identifiers that can be set as the selected task state filter identifier. | text | r |
| selected task state filter identifier | The currently selected task state filter identifier. | text | read/write |
| available task duration filter identifiers | The list of possible identifiers that can be set as the selected task duration filter identifier. | text | r |
| selected task duration filter identifier | The currently selected task duration filter identifier. | text | read/write |
| available task flagged filter identifiers | The list of possible identifiers that can be set as the selected task flagged filter identifier. | text | r |
| selected task flagged filter identifier | The currently selected task flagged filter identifier. | text | read/write |

<a name="inbox_tree"></a>
```yaml
---
type: class
name: inbox tree
suite: OmniFocus suite
---
```

## Class: inbox tree

**Description:** The tree in the sidebar representing the Inbox.

**Inherits:** tree

<a name="library_tree"></a>
```yaml
---
type: class
name: library tree
suite: OmniFocus suite
---
```

## Class: library tree

**Description:** The tree in the sidebar representing the top level library of objects.

**Inherits:** tree

<a name="perspective"></a>
```yaml
---
type: class
name: perspective
suite: OmniFocus suite
---
```

## Class: perspective

**Description:** A perspective.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the perspective. | text | read/write |
| name | The name of the perspective. | text | read/write |

<a name="builtin_perspective"></a>
```yaml
---
type: class
name: builtin perspective
suite: OmniFocus suite
---
```

## Class: builtin perspective

**Description:** A built-in perspective.

**Inherits:** perspective

<a name="custom_perspective"></a>
```yaml
---
type: class
name: custom perspective
suite: OmniFocus suite
---
```

## Class: custom perspective

**Description:** A user created perspective.

**Inherits:** perspective

<a name="project_status"></a>
```yaml
---
type: enumeration
name: project status
suite: OmniFocus suite
---
```

## Enumeration: project status

### Enumerators
| Name | Description |
|---|---|
| active status | Active |
| on hold status | On Hold |
| done status | Done |
| dropped status | Dropped |

<a name="interval_unit"></a>
```yaml
---
type: enumeration
name: interval unit
suite: OmniFocus suite
---
```

## Enumeration: interval unit

### Enumerators
| Name | Description |
|---|---|
| minute | Minutes |
| hour | Hours |
| day | Days |
| week | Weeks |
| month | Months |
| year | Years |

<a name="repetition_method"></a>
```yaml
---
type: enumeration
name: repetition method
suite: OmniFocus suite
---
```

## Enumeration: repetition method

### Enumerators
| Name | Description |
|---|---|
| fixed repetition | Repeat on a fixed schedule. |
| start after completion | Start again after completion. |
| due after completion | Due again after completion. |

<a name="location_trigger"></a>
```yaml
---
type: enumeration
name: location trigger
suite: OmniFocus suite
---
```

## Enumeration: location trigger

### Enumerators
| Name | Description |
|---|---|
| notify when arriving | notify when arriving at this location |
| notify when leaving | notify when leaving this location |

<a name="sidebar_tab"></a>
```yaml
---
type: enumeration
name: sidebar tab
suite: OmniFocus suite
---
```

## Enumeration: sidebar tab

### Enumerators
| Name | Description |
|---|---|
| inbox tab | inbox tab |
| projects tab | projects tab |
| tags tab | tags tab |
| forecast tab | forecast tab |
| flagged tab | flagged tab |
| review tab | review tab |

<a name="repetition_interval"></a>
```yaml
---
type: record-type
name: repetition interval
suite: OmniFocus suite
---
```

## Record Type: repetition interval

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| unit | The units of the repetition interval. | interval unit | read/write |
| steps | The count of the repetition interval. | integer | read/write |
| fixed | If fixed, the next repetition will be relative to a fixed calendar.  If sliding, the next repetition will be calculated when needed. | boolean | read/write |

<a name="repetition_rule"></a>
```yaml
---
type: record-type
name: repetition rule
suite: OmniFocus suite
---
```

## Record Type: repetition rule

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| repetition method | The repetition method. If fixed, the next repetition will be relative to a fixed calendar.  If sliding, the next repetition will be calculated when the action or inbox item is resolved. | repetition method | read/write |
| recurrence | The iCalendar (RFC 2445) string describing the recurrence. | text | read/write |

<a name="location_information"></a>
```yaml
---
type: record-type
name: location information
suite: OmniFocus suite
---
```

## Record Type: location information

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | A display name for the location. | text | read/write |
| latitude | Latitude in degrees from -90 to +90. | real | read/write |
| longitude | Longitude in degrees from -180 to +180. | real | read/write |
| altitude | Altitude in meters from sea level. | real | read/write |
| radius | Radius of accuracy in kilometers, from 0.1km to 10km. | real | read/write |
| trigger | Location notification trigger. | location trigger | read/write |

<a name="completion_match"></a>
```yaml
---
type: record-type
name: completion match
suite: OmniFocus suite
---
```

## Record Type: completion match

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The identifier of the matching object. | text | read/write |
| name | The name of the matching object. | text | read/write |
| score | The score of the match.  Larger scores are more relevant. | integer | read/write |
| xml | A xml string with <span> tags around the matched characters in the object's name. | text | read/write |

<a name="summarized_text_result"></a>
```yaml
---
type: record-type
name: summarized text result
suite: OmniFocus suite
---
```

## Record Type: summarized text result

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| summarized text | The summarized text. | text | read/write |
| was summarized | True if the text was summarized in addition to being normalized. | boolean | read/write |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: OmniFocus suite
---
```

## Class Extension: application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| build number | This is the build number of the application, for example 63.1 or 63.  Major and minor versions are separated by a dot.  So 63.10 comes after 63.1. | text | r |
| reference date | The date on from which the date collated smart groups are based.  When set, the reference date will be rounded to the first instant of the day of the specified date. | date | read/write |
| current time offset | The current time offset from a reference date. Useful for timing scripts. | real | read/write |
| default document | The user's default document. | document | read/write |
| quick entry | The Quick Entry panel for the default document. | quick entry tree | read/write |
| perspective names | The names of all available perspectives in the default document. | text | r |

### Elements
- **Type:** perspective
- **Type:** preference
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: OmniFocus suite
---
```

## Class Extension: document

**Description:** An OmniFocus document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The document's unique identifier. | text | r |
| can undo | Whether the document can undo the most recent command. | boolean | r |
| can redo | Whether the document can redo the most recently undone command. | boolean | r |
| will autosave | Whether the document will autosave. | boolean | read/write |
| compresses transactions | Whether the document will write compressed transactions to disk; defaults to true. | boolean | read/write |
| includes summaries | Whether the document will write computed summary information when writing transactions. | boolean | read/write |
| syncing | True if the document is currently syncing, false otherwise. | boolean | r |
| last sync date | Date of the last sync. | date | r |
| last sync error | Error message (if any) for the last sync. | text | r |
| quick entry | The Quick Entry panel for the document. | quick entry tree | read/write |
| disable automatic inbox cleanup | If set, automatic cleanup of inbox items won't happen. | boolean | read/write |
| path | The document's path on disk. | text | r |
| perspective names | The names of all available perspectives in this document. | text | r |

### Elements
- **Type:** setting
- **Type:** document window
- **Type:** section
- **Type:** folder
- **Type:** project
- **Type:** tag
- **Type:** deprecated context
- **Type:** inbox task
- **Type:** task
- **Type:** flattened task
- **Type:** flattened project
- **Type:** flattened folder
- **Type:** flattened tag
- **Type:** perspective
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
## Omni Tree Suite

**Description:** AppleScript commands and classes specific to Omni's outline trees

<a name="pbcopy"></a>
```yaml
---
type: command
name: pbcopy
suite: Omni Tree Suite
---
```

## Command: pbcopy

**Description:** Copies one or more nodes to the pasteboard.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| items | The items to copy the the pasteboard. | specifier, specifier | No |
| from | The tree to perform the copy. | tree | No |
| as | The list of type identifiers to use when copying the trees.  If omitted, all writable pasteboard types are used. | text, text | Yes |
| to | The name of the pasteboard to copy to. | text | Yes |

<a name="pbpaste"></a>
```yaml
---
type: command
name: pbpaste
suite: Omni Tree Suite
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
suite: Omni Tree Suite
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

<a name="tree"></a>
```yaml
---
type: class
name: tree
suite: Omni Tree Suite
---
```

## Class: tree

**Description:** A tree representing an object, along with its sub-trees.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the object being represented by this tree. | text | r |
| id | The identifier of object being represented by this tree. | text | r |
| value | The object being represented by this tree. | item | r |
| selected | This is true if the node is selected.  Note that attempts to set this while the node is not visible (collapsed parent, etc.) will silently do nothing. | boolean | read/write |
| expanded | This is true if the node is expanded. | boolean | read/write |
| note expanded | This is true if the node note is expanded. | boolean | read/write |
| writable pasteboard types | A list of the types that can be used when writing nodes to the pasteboard (i.e., copying). | pasteboard type | read/write |
| readable pasteboard types | A list of the types that can be used when reading nodes from the pasteboard (i.e., pasteing). | pasteboard type | read/write |

### Elements
- **Type:** tree
- **Type:** descendant tree
- **Type:** ancestor tree
- **Type:** leaf
- **Type:** preceding sibling
- **Type:** following sibling
- **Type:** selected tree
### Responds To
- **Command:** set
- **Command:** add
- **Command:** remove
- **Command:** pbpaste
<a name="descendant_tree"></a>
```yaml
---
type: class
name: descendant tree
suite: Omni Tree Suite
---
```

## Class: descendant tree

**Description:** All the descendant trees in the user-specified sort ordering, listing each tree, then its children and so forth.

**Inherits:** tree

<a name="ancestor_tree"></a>
```yaml
---
type: class
name: ancestor tree
suite: Omni Tree Suite
---
```

## Class: ancestor tree

**Description:** The ancestor trees of this tree.

**Inherits:** tree

<a name="leaf"></a>
```yaml
---
type: class
name: leaf
suite: Omni Tree Suite
---
```

## Class: leaf

**Description:** The descendants of a tree that have no children themselves.

**Inherits:** tree

<a name="following_sibling"></a>
```yaml
---
type: class
name: following sibling
suite: Omni Tree Suite
---
```

## Class: following sibling

**Description:** The sibling trees of this tree after it in the user-specified sort ordering.

**Inherits:** tree

<a name="preceding_sibling"></a>
```yaml
---
type: class
name: preceding sibling
suite: Omni Tree Suite
---
```

## Class: preceding sibling

**Description:** The sibling trees of this tree before it in the user-specified sort ordering.

**Inherits:** tree

<a name="selected_tree"></a>
```yaml
---
type: class
name: selected tree
suite: Omni Tree Suite
---
```

## Class: selected tree

**Description:** The trees of this tree that are selected in the user interface, possibly including this tree.

**Inherits:** tree

<a name="pasteboard_type"></a>
```yaml
---
type: record-type
name: pasteboard type
suite: Omni Tree Suite
---
```

## Record Type: pasteboard type

**Description:** A description of a pasteboard type.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | the unique identifier of the pasteboard type | text | read/write |
| name | the localized human-readable description of the pasteboard type | text | read/write |

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

