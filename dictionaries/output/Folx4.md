# Folx4 Terminology: AppleScript/JSX

## Table of Contents

### NSCoreSuite
#### Commands
- [open](#open)
- [print](#print)
- [quit](#quit)
- [close](#close)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [get](#get)
- [make](#make)
- [move](#move)
- [save](#save)
- [set](#set)
#### Classs
- [item](#item)
- [application](#application)
- [window](#window)
#### Enumerations
- [save options](#save_options)
### FolxSuite
#### Commands
- [srun](#srun)
- [add url](#add_url)
- [add URLs](#add_urls)
#### Classs
- [application](#application)


## NSCoreSuite

**Description:** Common classes and commands for most applications.

<a name="open"></a>
```yaml
---
type: command
name: open
suite: NSCoreSuite
---
```

## Command: open

**Description:** Open an object.

### Direct Parameter
- **Description:** The file(s) to be opened.
- **Types:** file
<a name="print"></a>
```yaml
---
type: command
name: print
suite: NSCoreSuite
---
```

## Command: print

**Description:** Print an object.

### Direct Parameter
- **Description:** The file(s) or document(s) to be printed.
- **Types:** file
<a name="quit"></a>
```yaml
---
type: command
name: quit
suite: NSCoreSuite
---
```

## Command: quit

**Description:** Quit an application.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Specifies whether changes should be saved before quitting. | save options | Yes |

<a name="close"></a>
```yaml
---
type: command
name: close
suite: NSCoreSuite
---
```

## Command: close

**Description:** Close an object.

### Direct Parameter
- **Description:** the object to close
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| saving | Specifies whether changes should be saved before closing. | save options | Yes |
| saving in | The file in which to save the object. | file | Yes |

<a name="count"></a>
```yaml
---
type: command
name: count
suite: NSCoreSuite
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
suite: NSCoreSuite
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
suite: NSCoreSuite
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
suite: NSCoreSuite
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
<a name="get"></a>
```yaml
---
type: command
name: get
suite: NSCoreSuite
---
```

## Command: get

**Description:** Get the data for an object.

### Direct Parameter
- **Types:** specifier
### Result
- **Types:** any
<a name="make"></a>
```yaml
---
type: command
name: make
suite: NSCoreSuite
---
```

## Command: make

**Description:** Make a new object.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| new | The class of the new object. | type | No |
| at | The location at which to insert the object. | location specifier | Yes |
| with data | The initial data for the object. | any | Yes |
| with properties | The initial values for properties of the object. | record | Yes |

### Result
- **Description:** to the new object
- **Types:** specifier
<a name="move"></a>
```yaml
---
type: command
name: move
suite: NSCoreSuite
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

<a name="save"></a>
```yaml
---
type: command
name: save
suite: NSCoreSuite
---
```

## Command: save

**Description:** Save an object.

### Direct Parameter
- **Description:** the object to save, usually a document or window
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The file in which to save the object. | file | Yes |
| as | The file type in which to save the data. | text | Yes |

<a name="set"></a>
```yaml
---
type: command
name: set
suite: NSCoreSuite
---
```

## Command: set

**Description:** Set an object's data.

### Direct Parameter
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new value. | any | No |

<a name="item"></a>
```yaml
---
type: class
name: item
suite: NSCoreSuite
---
```

## Class: item

**Description:** A scriptable object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| class | The class of the object. | type | r |
| properties | All of the object's properties. | record | read/write |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
- **Command:** None
<a name="application"></a>
```yaml
---
type: class
name: application
suite: NSCoreSuite
---
```

## Class: application

**Description:** An application's top level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the application. | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application. | text | r |

### Elements
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
suite: NSCoreSuite
---
```

## Class: window

**Description:** A window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The full title of the window. | text | read/write |
| id | The unique identifier of the window. | number | r |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Whether the window has a close box. | boolean | r |
| titled | Whether the window has a title bar. | boolean | r |
| index | The index of the window in the back-to-front window ordering. | number | read/write |
| floating | Whether the window floats. | boolean | r |
| miniaturizable | Whether the window can be miniaturized. | boolean | r |
| miniaturized | Whether the window is currently miniaturized. | boolean | read/write |
| modal | Whether the window is the application's current modal window. | boolean | r |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window can be zoomed. | boolean | r |
| zoomed | Whether the window is currently zoomed. | boolean | read/write |

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
<a name="save_options"></a>
```yaml
---
type: enumeration
name: save options
suite: NSCoreSuite
---
```

## Enumeration: save options

### Enumerators
| Name | Description |
|---|---|
| yes | Save the file. |
| no | Do not save the file. |
| ask | Ask the user whether or not to save the file. |

## FolxSuite

**Description:** Folx classes and commands.

<a name="srun"></a>
```yaml
---
type: command
name: srun
suite: FolxSuite
---
```

## Command: srun

**Description:** Run scheduled tasks

### Direct Parameter
- **Description:** command
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with param | Parameter | text | Yes |

<a name="add_url"></a>
```yaml
---
type: command
name: add url
suite: FolxSuite
---
```

## Command: add url

**Description:** Add url

### Direct Parameter
- **Description:** url string
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with title | title of url | text | Yes |
| with referrer | referrer of url | text | Yes |
| from application | sender | text | Yes |
| with cookie | cookie for url | text | Yes |

<a name="add_urls"></a>
```yaml
---
type: command
name: add URLs
suite: FolxSuite
---
```

## Command: add URLs

**Description:** Adds new downloads to Folx

### Direct Parameter
- **Description:** urls string
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with referrer | referrer | text | Yes |
| with cookies | cookies | text | Yes |
| with post data | post data | text | Yes |
| with titles | titles | text | Yes |
| from application | from application | text | Yes |

<a name="application"></a>
```yaml
---
type: class
name: application
suite: FolxSuite
---
```

## Class: application

**Description:** An application's top level scripting object.

**Inherits:** application

### Responds To
- **Command:** None
- **Command:** None
- **Command:** None
