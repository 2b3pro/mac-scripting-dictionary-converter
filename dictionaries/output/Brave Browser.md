# Brave Browser: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [save](#save)
- [open](#open)
- [close](#close)
- [quit](#quit)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [make](#make)
- [move](#move)
- [print](#print)
#### Classs
- [application](#application)
- [window](#window)
### Chromium Suite
#### Commands
- [reload](#reload)
- [go back](#go_back)
- [go forward](#go_forward)
- [select all](#select_all)
- [cut selection](#cut_selection)
- [copy selection](#copy_selection)
- [paste selection](#paste_selection)
- [undo](#undo)
- [redo](#redo)
- [stop](#stop)
- [view source](#view_source)
- [execute](#execute)
#### Classs
- [tab](#tab)
- [bookmark folder](#bookmark_folder)
- [bookmark item](#bookmark_item)
#### Class Extensions
- [application](#application)


## Standard Suite

**Description:** Common classes and commands for all applications.

<a name="save"></a>
```yaml
---
type: command
name: save
suite: Standard Suite
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
| as | The file type in which to save the data. Can be 'only html', 'complete html', or 'single file'; default is 'complete html'. | text | Yes |

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

**Description:** Close a window.

### Direct Parameter
- **Description:** the document(s) or window(s) to close.
- **Types:** specifier
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
<a name="print"></a>
```yaml
---
type: command
name: print
suite: Standard Suite
---
```

## Command: print

**Description:** Print an object.

### Direct Parameter
- **Description:** The file(s) or document(s) to be printed.
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
- **Type:** window
### Responds To
- **Command:** open
- **Command:** print
- **Command:** quit
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
| given name | The given name of the window. | text | read/write |
| name | The full title of the window. | text | r |
| id | The unique identifier of the window. | text | r |
| index | The index of the window, ordered front to back. | integer | read/write |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Whether the window has a close box. | boolean | r |
| minimizable | Whether the window can be minimized. | boolean | r |
| minimized | Whether the window is currently minimized. | boolean | read/write |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window can be zoomed. | boolean | r |
| zoomed | Whether the window is currently zoomed. | boolean | read/write |
| active tab | Returns the currently selected tab | tab | r |
| mode | Represents the mode of the window which can be 'normal' or 'incognito', can be set only once during creation of the window. | text | read/write |
| active tab index | The index of the active tab. | integer | read/write |

### Elements
- **Type:** tab
### Responds To
- **Command:** close
## Chromium Suite

**Description:** Common classes and commands for Chrome.

<a name="reload"></a>
```yaml
---
type: command
name: reload
suite: Chromium Suite
---
```

## Command: reload

**Description:** Reload a tab.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="go_back"></a>
```yaml
---
type: command
name: go back
suite: Chromium Suite
---
```

## Command: go back

**Description:** Go Back (If Possible).

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="go_forward"></a>
```yaml
---
type: command
name: go forward
suite: Chromium Suite
---
```

## Command: go forward

**Description:** Go Forward (If Possible).

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="select_all"></a>
```yaml
---
type: command
name: select all
suite: Chromium Suite
---
```

## Command: select all

**Description:** Select all.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="cut_selection"></a>
```yaml
---
type: command
name: cut selection
suite: Chromium Suite
---
```

## Command: cut selection

**Description:** Cut selected text (If Possible).

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="copy_selection"></a>
```yaml
---
type: command
name: copy selection
suite: Chromium Suite
---
```

## Command: copy selection

**Description:** Copy text.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="paste_selection"></a>
```yaml
---
type: command
name: paste selection
suite: Chromium Suite
---
```

## Command: paste selection

**Description:** Paste text (If Possible).

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="undo"></a>
```yaml
---
type: command
name: undo
suite: Chromium Suite
---
```

## Command: undo

**Description:** Undo the last change.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="redo"></a>
```yaml
---
type: command
name: redo
suite: Chromium Suite
---
```

## Command: redo

**Description:** Redo the last change.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="stop"></a>
```yaml
---
type: command
name: stop
suite: Chromium Suite
---
```

## Command: stop

**Description:** Stop the current tab from loading.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="view_source"></a>
```yaml
---
type: command
name: view source
suite: Chromium Suite
---
```

## Command: view source

**Description:** View the HTML source of the tab.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
<a name="execute"></a>
```yaml
---
type: command
name: execute
suite: Chromium Suite
---
```

## Command: execute

**Description:** Execute a piece of javascript.

### Direct Parameter
- **Description:** The tab to execute the command in.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| javascript | The javascript code to execute. | text | No |

### Result
- **Types:** any
<a name="tab"></a>
```yaml
---
type: class
name: tab
suite: Chromium Suite
---
```

## Class: tab

**Description:** A tab.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | Unique ID of the tab. | text | r |
| title | The title of the tab. | text | r |
| URL | The url visible to the user. | text | read/write |
| loading | Is loading? | boolean | r |

### Responds To
- **Command:** undo
- **Command:** redo
- **Command:** cut selection
- **Command:** copy selection
- **Command:** paste selection
- **Command:** select all
- **Command:** go back
- **Command:** go forward
- **Command:** reload
- **Command:** stop
- **Command:** print
- **Command:** view source
- **Command:** save
- **Command:** close
- **Command:** execute
<a name="bookmark_folder"></a>
```yaml
---
type: class
name: bookmark folder
suite: Chromium Suite
---
```

## Class: bookmark folder

**Description:** A bookmarks folder that contains other bookmarks folder and bookmark items.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | Unique ID of the bookmark folder. | text | r |
| title | The title of the folder. | text | read/write |
| index | Returns the index with respect to its parent bookmark folder. | number | r |

### Elements
- **Type:** bookmark folder
- **Type:** bookmark item
<a name="bookmark_item"></a>
```yaml
---
type: class
name: bookmark item
suite: Chromium Suite
---
```

## Class: bookmark item

**Description:** An item consists of an URL and the title of a bookmark

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | Unique ID of the bookmark item. | text | r |
| title | The title of the bookmark item. | text | read/write |
| URL | The URL of the bookmark. | text | read/write |
| index | Returns the index with respect to its parent bookmark folder. | number | r |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Chromium Suite
---
```

## Class Extension: application

**Description:** The application's top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| bookmarks bar | The bookmarks bar bookmark folder. | bookmark folder | r |
| other bookmarks | The other bookmarks bookmark folder. | bookmark folder | r |

### Elements
- **Type:** bookmark folder
