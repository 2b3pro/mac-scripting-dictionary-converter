# MacDown Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [open](#open)
- [close](#close)
- [save](#save)
- [quit](#quit)
- [make](#make)
#### Classs
- [application](#application)
- [window](#window)
#### Enumerations
- [save options](#save_options)
### Text Suite
#### Classs
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
### MacDown Suite
#### Classs
- [document](#document)
#### Enumerations
- [saveable file format](#saveable_file_format)


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

**Description:** Open a document.

### Direct Parameter
- **Description:** The file(s) to be opened.
- **Types:** file
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
| as | The file format to use. | saveable file format | Yes |

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
- **Command:** None
- **Command:** None
- **Command:** None
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
- **Command:** None
- **Command:** None
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

## Text Suite

**Description:** Common text classes for all applications.

<a name="character"></a>
```yaml
---
type: class
name: character
suite: Text Suite
---
```

## Class: character

**Description:** One of some text's characters.

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: Text Suite
---
```

## Class: paragraph

**Description:** One of some text's paragraphs.

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
<a name="word"></a>
```yaml
---
type: class
name: word
suite: Text Suite
---
```

## Class: word

**Description:** One of some text's words.

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
## MacDown Suite

**Description:** MacDown specific classes.

<a name="document"></a>
```yaml
---
type: class
name: document
suite: MacDown Suite
---
```

## Class: document

**Description:** A MacDown document.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | Its name. | text | r |
| modified | Has it been modified since the last save? | boolean | r |
| file | Its location on disk, if it has one. | file | r |
| text | Source in the document. | text | rw |
| html | Rendered HTML of the document. | text | r |

### Responds To
- **Command:** None
- **Command:** None
<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: MacDown Suite
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| Markdown | Markdown format |
| Text | Plain text format |
| Data | Raw bytes format |

