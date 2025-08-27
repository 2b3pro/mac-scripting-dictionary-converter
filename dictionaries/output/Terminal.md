# Terminal Terminology: AppleScript/JSX

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
- [window](#window)
#### Enumerations
- [save options](#save_options)
- [printing error handling](#printing_error_handling)
#### Record Types
- [print settings](#print_settings)
### Terminal Suite
#### Commands
- [do script](#do_script)
- [get URL](#get_url)
#### Classs
- [settings set](#settings_set)
- [tab](#tab)
#### Value Types
- [color](#color)
#### Class Extensions
- [application](#application)


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
| to | The location for the new object(s). | location specifier | No |
| with properties | Properties to be set in the new duplicated object(s). | record | Yes |

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
- **Types:** specifier
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

<a name="application"></a>
```yaml
---
type: class
name: application
suite: Standard Suite
---
```

## Class: application

**Description:** The application‘s top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application. | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application. | text | r |

### Elements
- **Type:** window
### Responds To
- **Command:** open
- **Command:** print
- **Command:** quit
- **Command:** get URL
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
| miniaturizable | Whether the window can be minimized. | boolean | r |
| miniaturized | Whether the window is currently minimized. | boolean | read/write |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window can be zoomed. | boolean | r |
| zoomed | Whether the window is currently zoomed. | boolean | read/write |
| frontmost | Whether the window is currently the frontmost Terminal window. | boolean | read/write |
| position | The position of the window, relative to the upper left corner of the screen. | point | read/write |
| origin | The position of the window, relative to the lower left corner of the screen. | point | read/write |
| size | The width and height of the window | point | read/write |
| frame | The bounding rectangle, relative to the lower left corner of the screen. | rectangle | read/write |

### Elements
- **Type:** tab
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
| error handling | how errors are handled | printing error handling | read/write |
| fax number | for fax number | text | read/write |
| target printer | for target printer | text | read/write |

## Terminal Suite

**Description:** Terminal specific classes.

<a name="do_script"></a>
```yaml
---
type: command
name: do script
suite: Terminal Suite
---
```

## Command: do script

**Description:** Runs a UNIX shell script or command.

### Direct Parameter
- **Description:** The command to execute.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with command | Data to be passed to the Terminal application as the command line. Deprecated; use direct parameter instead. | text, any | Yes |
| in | The tab in which to execute the command | tab, window, any | Yes |

### Result
- **Description:** The tab the command was executed in.
- **Types:** tab
<a name="get_url"></a>
```yaml
---
type: command
name: get URL
suite: Terminal Suite
---
```

## Command: get URL

**Description:** Open a command an ssh, telnet, or x-man-page URL.

### Direct Parameter
- **Description:** The URL to open.
- **Types:** text
<a name="settings_set"></a>
```yaml
---
type: class
name: settings set
suite: Terminal Suite
---
```

## Class: settings set

**Description:** A set of settings.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the settings set. | integer | r |
| name | The name of the settings set. | text | read/write |
| number of rows | The number of rows displayed in the tab. | integer | read/write |
| number of columns | The number of columns displayed in the tab. | integer | read/write |
| cursor color | The cursor color for the tab. | color | read/write |
| background color | The background color for the tab. | color | read/write |
| normal text color | The normal text color for the tab. | color | read/write |
| bold text color | The bold text color for the tab. | color | read/write |
| font name | The name of the font used to display the tab’s contents. | text | read/write |
| font size | The size of the font used to display the tab’s contents. | integer | read/write |
| font antialiasing | Whether the font used to display the tab’s contents is antialiased. | boolean | read/write |
| clean commands | The processes which will be ignored when checking whether a tab can be closed without showing a prompt. | text | read/write |
| title displays device name | Whether the title contains the device name. | boolean | read/write |
| title displays shell path | Whether the title contains the shell path. | boolean | read/write |
| title displays window size | Whether the title contains the tab’s size, in rows and columns. | boolean | read/write |
| title displays settings name | Whether the title contains the settings name. | boolean | read/write |
| title displays custom title | Whether the title contains a custom title. | boolean | read/write |
| custom title | The tab’s custom title. | text | read/write |

<a name="tab"></a>
```yaml
---
type: class
name: tab
suite: Terminal Suite
---
```

## Class: tab

**Description:** A tab.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| number of rows | The number of rows displayed in the tab. | integer | read/write |
| number of columns | The number of columns displayed in the tab. | integer | read/write |
| contents | The currently visible contents of the tab. | text | r |
| history | The contents of the entire scrolling buffer of the tab. | text | r |
| busy | Whether the tab is busy running a process. | boolean | r |
| processes | The processes currently running in the tab. | text | r |
| selected | Whether the tab is selected. | boolean | read/write |
| title displays custom title | Whether the title contains a custom title. | boolean | read/write |
| custom title | The tab’s custom title. | text | read/write |
| tty | The tab’s TTY device. | text | r |
| current settings | The set of settings which control the tab’s behavior and appearance. | settings set | read/write |
| cursor color | The cursor color for the tab. | color | read/write |
| background color | The background color for the tab. | color | read/write |
| normal text color | The normal text color for the tab. | color | read/write |
| bold text color | The bold text color for the tab. | color | read/write |
| clean commands | The processes which will be ignored when checking whether a tab can be closed without showing a prompt. | text | read/write |
| title displays device name | Whether the title contains the device name. | boolean | read/write |
| title displays shell path | Whether the title contains the shell path. | boolean | read/write |
| title displays window size | Whether the title contains the tab’s size, in rows and columns. | boolean | read/write |
| title displays file name | Whether the title contains the file name. | boolean | read/write |
| font name | The name of the font used to display the tab’s contents. | text | read/write |
| font size | The size of the font used to display the tab’s contents. | integer | read/write |
| font antialiasing | Whether the font used to display the tab’s contents is antialiased. | boolean | read/write |

<a name="color"></a>
```yaml
---
type: value-type
name: color
suite: Terminal Suite
---
```

## Value Type: color

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Terminal Suite
---
```

## Class Extension: application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| default settings | The settings set used for new windows. | settings set | read/write |
| startup settings | The settings set used for the window created on application startup. | settings set | read/write |

### Elements
- **Type:** settings set
