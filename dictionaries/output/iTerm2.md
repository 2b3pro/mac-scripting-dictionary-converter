# iTerm2 Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
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
### iTerm2 Suite
#### Commands
- [close](#close)
- [request cookie](#request_cookie)
- [create tab](#create_tab)
- [create tab with default profile](#create_tab_with_default_profile)
- [create window with profile](#create_window_with_profile)
- [create hotkey window with profile](#create_hotkey_window_with_profile)
- [launch API script named](#launch_api_script_named)
- [invoke API expression](#invoke_api_expression)
- [create window with default profile](#create_window_with_default_profile)
- [write](#write)
- [select](#select)
- [split vertically](#split_vertically)
- [split vertically with default profile](#split_vertically_with_default_profile)
- [split vertically with same profile](#split_vertically_with_same_profile)
- [split horizontally](#split_horizontally)
- [split horizontally with default profile](#split_horizontally_with_default_profile)
- [split horizontally with same profile](#split_horizontally_with_same_profile)
- [variable](#variable)
- [set variable](#set_variable)
- [reveal hotkey window](#reveal_hotkey_window)
- [hide hotkey window](#hide_hotkey_window)
- [toggle hotkey window](#toggle_hotkey_window)
#### Classs
- [tab](#tab)
- [session](#session)
#### Value Types
- [RGB color](#rgb_color)


## Standard Suite

**Description:** Common classes and commands for all applications.

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

**Description:** The application's top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| current window | The frontmost window | window | read/write |
| name | The name of the application. | text | r |
| frontmost | Is this the frontmost (active) application? | boolean | r |
| version | The version of the application. | text | r |

### Elements
- **Type:** window
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
| id | The unique identifier of the session. | integer | r |
| alternate identifier | The alternate unique identifier of the session. | text | r |
| name | The full title of the window. | text | r |
| index | The index of the window, ordered front to back. | integer | read/write |
| bounds | The bounding rectangle of the window. | rectangle | read/write |
| closeable | Whether the window has a close box. | boolean | r |
| miniaturizable | Whether the window can be minimized. | boolean | r |
| miniaturized | Whether the window is currently minimized. | boolean | read/write |
| resizable | Whether the window can be resized. | boolean | r |
| visible | Whether the window is currently visible. | boolean | read/write |
| zoomable | Whether the window can be zoomed. | boolean | r |
| zoomed | Whether the window is currently zoomed. | boolean | read/write |
| frontmost | Whether the window is currently the frontmost window. | boolean | read/write |
| current tab | The currently selected tab | tab | read/write |
| current session | The current session in a window | session | read/write |
| is hotkey window | Whether the window is a hotkey window. | boolean | read/write |
| hotkey window profile | If the window is a hotkey window, this gives the name of the profile that created the window.  | text | read/write |
| position | The position of the window, relative to the upper left corner of the screen. | point | read/write |
| origin | The position of the window, relative to the lower left corner of the screen. | point | read/write |
| size | The width and height of the window | point | read/write |
| frame | The bounding rectangle, relative to the lower left corner of the screen. | rectangle | read/write |

### Elements
- **Type:** tab
### Responds To
- **Command:** close
- **Command:** select
- **Command:** create tab with default profile
- **Command:** create tab
- **Command:** reveal hotkey window
- **Command:** hide hotkey window
- **Command:** toggle hotkey window
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

## iTerm2 Suite

**Description:** Classes just for the iTerm2 application.

<a name="close"></a>
```yaml
---
type: command
name: close
suite: iTerm2 Suite
---
```

## Command: close

**Description:** Close a document.

### Direct Parameter
- **Description:** the session, tab, or window to close.
- **Types:** specifier
<a name="request_cookie"></a>
```yaml
---
type: command
name: request cookie
suite: iTerm2 Suite
---
```

## Command: request cookie

**Description:** Request a Python API cookie

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| and key for app named | Name of script using the cookie. This is shown in the console. | text | Yes |

### Result
- **Description:** A cookie that can be used to connect to the Python API endpoint
- **Types:** text
<a name="create_tab"></a>
```yaml
---
type: command
name: create tab
suite: iTerm2 Suite
---
```

## Command: create tab

**Description:** Create a new tab

### Direct Parameter
- **Description:** the session, tab, or window to close.
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with profile | The profile name | text | No |
| command | Shell command to run | text | Yes |

### Result
- **Description:** The tab that was created
- **Types:** tab
<a name="create_tab_with_default_profile"></a>
```yaml
---
type: command
name: create tab with default profile
suite: iTerm2 Suite
---
```

## Command: create tab with default profile

**Description:** Create a new tab with the default profile

### Direct Parameter
- **Description:** The window in which to create a new tab
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The tab that was created
- **Types:** tab
<a name="create_window_with_profile"></a>
```yaml
---
type: command
name: create window with profile
suite: iTerm2 Suite
---
```

## Command: create window with profile

**Description:** Create a new window

### Direct Parameter
- **Description:** The profile name
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The window that was created
- **Types:** window
<a name="create_hotkey_window_with_profile"></a>
```yaml
---
type: command
name: create hotkey window with profile
suite: iTerm2 Suite
---
```

## Command: create hotkey window with profile

**Description:** Create a hotkey window

### Direct Parameter
- **Description:** The profile name
- **Types:** text
### Result
- **Description:** The window that was created
- **Types:** window
<a name="launch_api_script_named"></a>
```yaml
---
type: command
name: launch API script named
suite: iTerm2 Suite
---
```

## Command: launch API script named

**Description:** Launch API script by name

### Direct Parameter
- **Description:** The script’s name
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| arguments | Arguments to pass to script | text | Yes |

<a name="invoke_api_expression"></a>
```yaml
---
type: command
name: invoke API expression
suite: iTerm2 Suite
---
```

## Command: invoke API expression

**Description:** Invokes an expression, such as a registered function.

### Direct Parameter
- **Description:** The expression to invoke, such as a function call.
- **Types:** text
### Result
- **Description:** String representation of the result, if available. Function calls’ return values are not available.
- **Types:** text
<a name="create_window_with_default_profile"></a>
```yaml
---
type: command
name: create window with default profile
suite: iTerm2 Suite
---
```

## Command: create window with default profile

**Description:** Create a new window with the default profile

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The window that was created
- **Types:** window
<a name="write"></a>
```yaml
---
type: command
name: write
suite: iTerm2 Suite
---
```

## Command: write

**Description:** Send text as though it was typed.

### Direct Parameter
- **Description:** The session to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| contents of file | Filename to send the contents of | file | Yes |
| text | Text to send | text | Yes |
| newline | If newline should be added to end of text (default: yes) | boolean | Yes |

<a name="select"></a>
```yaml
---
type: command
name: select
suite: iTerm2 Suite
---
```

## Command: select

**Description:** Make receiver visible and selected.

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
<a name="split_vertically"></a>
```yaml
---
type: command
name: split vertically
suite: iTerm2 Suite
---
```

## Command: split vertically

**Description:** Split a session vertically.

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with profile | Name of profile for new session. | text | No |
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="split_vertically_with_default_profile"></a>
```yaml
---
type: command
name: split vertically with default profile
suite: iTerm2 Suite
---
```

## Command: split vertically with default profile

**Description:** Split a session vertically, using the default profile for the new session

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="split_vertically_with_same_profile"></a>
```yaml
---
type: command
name: split vertically with same profile
suite: iTerm2 Suite
---
```

## Command: split vertically with same profile

**Description:** Split a session vertically, using the original session's profile for the new session

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="split_horizontally"></a>
```yaml
---
type: command
name: split horizontally
suite: iTerm2 Suite
---
```

## Command: split horizontally

**Description:** Split a session horizontally.

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with profile | Name of profile for new session. | text | No |
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="split_horizontally_with_default_profile"></a>
```yaml
---
type: command
name: split horizontally with default profile
suite: iTerm2 Suite
---
```

## Command: split horizontally with default profile

**Description:** Split a session horizontally, using the default profile for the new session

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="split_horizontally_with_same_profile"></a>
```yaml
---
type: command
name: split horizontally with same profile
suite: iTerm2 Suite
---
```

## Command: split horizontally with same profile

**Description:** Split a session horizontally, using the original session's profile for the new session

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| command | Shell command to run | text | Yes |

### Result
- **Description:** The session that was created
- **Types:** session
<a name="variable"></a>
```yaml
---
type: command
name: variable
suite: iTerm2 Suite
---
```

## Command: variable

**Description:** Returns the value of a session variable with the given name

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| named | Name of variable | text | No |

### Result
- **Description:** The variable's value
- **Types:** text
<a name="set_variable"></a>
```yaml
---
type: command
name: set variable
suite: iTerm2 Suite
---
```

## Command: set variable

**Description:** Sets the value of a session variable

### Direct Parameter
- **Description:** The object to send to
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| named | Name of variable | text | No |
| to | New value | text | No |

### Result
- **Description:** The variable's value
- **Types:** text
<a name="reveal_hotkey_window"></a>
```yaml
---
type: command
name: reveal hotkey window
suite: iTerm2 Suite
---
```

## Command: reveal hotkey window

**Description:** Reveals a hotkey window. Only to be called on windows that are hotkey windows.

### Direct Parameter
- **Description:** The window in which to create a new tab
- **Types:** specifier
<a name="hide_hotkey_window"></a>
```yaml
---
type: command
name: hide hotkey window
suite: iTerm2 Suite
---
```

## Command: hide hotkey window

**Description:** Hides a hotkey window. Only to be called on windows that are hotkey windows.

### Direct Parameter
- **Description:** The window in which to create a new tab
- **Types:** specifier
<a name="toggle_hotkey_window"></a>
```yaml
---
type: command
name: toggle hotkey window
suite: iTerm2 Suite
---
```

## Command: toggle hotkey window

**Description:** Toggles the visibility of a hotkey window. Only to be called on windows that are hotkey windows.

### Direct Parameter
- **Description:** The window in which to create a new tab
- **Types:** specifier
<a name="tab"></a>
```yaml
---
type: class
name: tab
suite: iTerm2 Suite
---
```

## Class: tab

**Description:** A terminal tab

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| current session | The current session in a tab | session | read/write |
| index | Index of tab in parent tab view control | integer | read/write |

### Elements
- **Type:** session
### Responds To
- **Command:** close
- **Command:** select
<a name="session"></a>
```yaml
---
type: class
name: session
suite: iTerm2 Suite
---
```

## Class: session

**Description:** A terminal session

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the session. | text | r |
| is processing | The session has received output recently. | boolean | read/write |
| is at shell prompt | The terminal is at the shell prompt. Requires shell integration. | boolean | read/write |
| columns |  | integer | read/write |
| rows |  | integer | read/write |
| tty |  | text | r |
| contents | The currently visible contents of the session. | text | read/write |
| text | The currently visible contents of the session. | text | r |
| color preset |  | text | read/write |
| background color |  | RGB color | read/write |
| bold color |  | RGB color | read/write |
| cursor color |  | RGB color | read/write |
| cursor text color |  | RGB color | read/write |
| foreground color |  | RGB color | read/write |
| selected text color |  | RGB color | read/write |
| selection color |  | RGB color | read/write |
| ANSI black color |  | RGB color | read/write |
| ANSI red color |  | RGB color | read/write |
| ANSI green color |  | RGB color | read/write |
| ANSI yellow color |  | RGB color | read/write |
| ANSI blue color |  | RGB color | read/write |
| ANSI magenta color |  | RGB color | read/write |
| ANSI cyan color |  | RGB color | read/write |
| ANSI white color |  | RGB color | read/write |
| ANSI bright black color |  | RGB color | read/write |
| ANSI bright red color |  | RGB color | read/write |
| ANSI bright green color |  | RGB color | read/write |
| ANSI bright yellow color |  | RGB color | read/write |
| ANSI bright blue color |  | RGB color | read/write |
| ANSI bright magenta color |  | RGB color | read/write |
| ANSI bright cyan color |  | RGB color | read/write |
| ANSI bright white color |  | RGB color | read/write |
| underline color |  | RGB color | read/write |
| use underline color | Whether the use a dedicated color for underlining. | boolean | read/write |
| background image |  | text | read/write |
| name |  | text | read/write |
| transparency |  | real | read/write |
| unique ID |  | text | r |
| profile name | The session's profile name | text | r |
| answerback string | ENQ Answerback string | text | read/write |

### Responds To
- **Command:** close
- **Command:** write
- **Command:** select
- **Command:** split vertically
- **Command:** split vertically with default profile
- **Command:** split vertically with same profile
- **Command:** split horizontally
- **Command:** split horizontally with default profile
- **Command:** split horizontally with same profile
- **Command:** variable
- **Command:** set variable
<a name="rgb_color"></a>
```yaml
---
type: value-type
name: RGB color
suite: iTerm2 Suite
---
```

## Value Type: RGB color

