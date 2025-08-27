# Scrivener: AppleScript/JSX

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
#### Classs
- [application](#application)
- [document](#document)
- [window](#window)
#### Enumerations
- [save options](#save_options)
- [printing error handling](#printing_error_handling)
#### Record Types
- [print settings](#print_settings)
### Text Suite
#### Classs
- [rich text](#rich_text)
- [character](#character)
- [paragraph](#paragraph)
- [word](#word)
- [attribute run](#attribute_run)
- [attachment](#attachment)
#### Value Types
- [color](#color)


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
| saving | Whether or not changes should be saved before closing. | save options | Yes |
| saving in | The file in which to save the document. | file | Yes |

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
| as | The type of file to save. | text | Yes |

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
| saving | Whether or not changed documents should be saved before closing. | save options | Yes |

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
- **Description:** the object whose elements are to be counted
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| each | The class of objects to be counted. | type | Yes |

### Result
- **Description:** the number of elements
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
- **Description:** the object to delete
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

**Description:** Copy object(s) and put the copies at a new location.

### Direct Parameter
- **Description:** the object(s) to duplicate
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new object(s). | location specifier | Yes |
| with properties | Properties to be set in the new duplicated object(s). | record | Yes |

### Result
- **Description:** the duplicated object(s)
- **Types:** specifier
<a name="exists"></a>
```yaml
---
type: command
name: exists
suite: Standard Suite
---
```

## Command: exists

**Description:** Verify if an object exists.

### Direct Parameter
- **Description:** the object in question
- **Types:** any
### Result
- **Description:** true if it exists, false if not
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

**Description:** Make a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object. | type | No |
| at | The location at which to insert the object. | location specifier | Yes |
| with data | The initial contents of the object. | any | Yes |
| with properties | The initial values for properties of the object. | record | Yes |

### Result
- **Description:** to the new object
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

**Description:** Move object(s) to a new location.

### Direct Parameter
- **Description:** the object(s) to move
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new location for the object(s). | location specifier | No |

### Result
- **Description:** the moved object(s)
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
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application. | text | r |

### Elements
- **Type:** document
- **Type:** window
### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
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
| name | The document's name. | text | r |
| modified | Has the document been modified since the last save? | boolean | r |
| file | The document's location on disk. | file | r |

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
| name | The full title of the window. | text | r |
| id | The unique identifier of the window. | integer | r |
| index | The index of the window, ordered front to back. | integer | read/write |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Whether the window has a close box. | boolean | r |
| minimizable | Whether the window can be minimized. | boolean | r |
| minimized | Whether the window is currently minimized. | boolean | read/write |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window can be zoomed. | boolean | r |
| zoomed | Whether the window is currently zoomed. | boolean | read/write |
| document | The document whose contents are being displayed in the window. | document | r |

### Responds To
- **Command:** None
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
| error handling | how errors are handled | printing error handling | read/write |
| fax number | for fax number | text | read/write |
| target printer | for target printer | text | read/write |

## Text Suite

**Description:** A set of basic classes for text processing.

<a name="rich_text"></a>
```yaml
---
type: class
name: rich text
suite: Text Suite
---
```

## Class: rich text

**Description:** Rich (styled) text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
<a name="character"></a>
```yaml
---
type: class
name: character
suite: Text Suite
---
```

## Class: character

**Description:** This subdivides the text into characters.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: Text Suite
---
```

## Class: paragraph

**Description:** This subdivides the text into paragraphs.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
<a name="word"></a>
```yaml
---
type: class
name: word
suite: Text Suite
---
```

## Class: word

**Description:** This subdivides the text into words.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
<a name="attribute_run"></a>
```yaml
---
type: class
name: attribute run
suite: Text Suite
---
```

## Class: attribute run

**Description:** This subdivides the text into chunks that all have the same attributes.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | integer | read/write |

### Elements
- **Type:** character
- **Type:** paragraph
- **Type:** word
- **Type:** attribute run
- **Type:** attachment
<a name="attachment"></a>
```yaml
---
type: class
name: attachment
suite: Text Suite
---
```

## Class: attachment

**Description:** Represents an inline text attachment. This class is used mainly for make commands.

**Inherits:** rich text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The path to the file for the attachment | text | read/write |

<a name="color"></a>
```yaml
---
type: value-type
name: color
suite: Text Suite
---
```

## Value Type: color

