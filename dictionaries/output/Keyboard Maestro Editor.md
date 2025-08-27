# Keyboard Maestro Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [open](#open)
- [close](#close)
- [quit](#quit)
- [count](#count)
- [delete](#delete)
- [duplicate](#duplicate)
- [exists](#exists)
- [make](#make)
- [move](#move)
- [select](#select)
- [edit](#edit)
#### Classs
- [application](#application)
- [window](#window)
### Keyboard Maestro Suite
#### Commands
- [setMacroEnable](#setmacroenable)
- [editMacro](#editmacro)
- [selectedMacros](#selectedmacros)
- [selectAction](#selectaction)
- [importMacros](#importmacros)
- [deleteMacro](#deletemacro)
- [deleteMacroGroup](#deletemacrogroup)
- [reload](#reload)
- [show preference pane](#show_preference_pane)
#### Classs
- [application](#application)
- [macro group](#macro_group)
- [smart group](#smart_group)
- [disabled macro group holder](#disabled_macro_group_holder)
- [macro](#macro)
- [trigger](#trigger)
- [action](#action)
- [case entry](#case_entry)
- [action list](#action_list)
### Standard URL Suite
#### Commands
- [geturl](#geturl)


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
- **Types:** file, file
### Result
- **Description:** The opened document(s).
- **Types:** file, file
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
- **Types:** list of specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new copy or copies. | location specifier | Yes |

### Result
- **Description:** The duplicated objects.
- **Types:** list of specifier
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
- **Types:** list of specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new location for the object(s). | location specifier | No |

### Result
- **Description:** The moved objects.
- **Types:** list of specifier
<a name="select"></a>
```yaml
---
type: command
name: select
suite: Standard Suite
---
```

## Command: select

**Description:** Select the specified object(s)

### Direct Parameter
- **Description:** the object to select
- **Types:** specifier
<a name="edit"></a>
```yaml
---
type: command
name: edit
suite: Standard Suite
---
```

## Command: edit

**Description:** Edit the specified object(s)

### Direct Parameter
- **Description:** the object to select
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
| selection | the selection in the macro editor | list of specifier | read/write |

### Elements
- **Type:** window
### Responds To
- **Command:** open
- **Command:** print
- **Command:** quit
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
| editing | Is the editor window editing right now? | boolean | rw |
| divider1 | Position of divider 1 | integer | rw |
| divider2 | Position of divider 2 | integer | rw |

### Responds To
- **Command:** close
## Keyboard Maestro Suite

**Description:** Terms specific to Keyboard Maestro.

<a name="setmacroenable"></a>
```yaml
---
type: command
name: setMacroEnable
suite: Keyboard Maestro Suite
---
```

## Command: setMacroEnable

**Description:** Enables or Disabled a Macro Group or Macro by name or UID.

### Direct Parameter
- **Description:** The name or UID of Macro Group or Macro.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| enable | enable or disable the Macro Group or Macro. | boolean | No |

<a name="editmacro"></a>
```yaml
---
type: command
name: editMacro
suite: Keyboard Maestro Suite
---
```

## Command: editMacro

**Description:** Start editing a Macro Group or Macro by name or UID.

### Direct Parameter
- **Description:** The name or UID of Macro Group or Macro.
- **Types:** text
<a name="selectedmacros"></a>
```yaml
---
type: command
name: selectedMacros
suite: Keyboard Maestro Suite
---
```

## Command: selectedMacros

**Description:** Selected Macro Group or Macro UIDs.

### Result
- **Description:** The UID of the selected Macro Group or Macros.
- **Types:** text
<a name="selectaction"></a>
```yaml
---
type: command
name: selectAction
suite: Keyboard Maestro Suite
---
```

## Command: selectAction

**Description:** Selected action by UID.

### Direct Parameter
- **Description:** The UID of the action to select.
- **Types:** integer
<a name="importmacros"></a>
```yaml
---
type: command
name: importMacros
suite: Keyboard Maestro Suite
---
```

## Command: importMacros

**Description:** Import macros

### Direct Parameter
- **Description:** URL to kmmacros file or the XML of the macros to import
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| disabled | force disable the imported Macros or Macro Groups | boolean | Yes |

<a name="deletemacro"></a>
```yaml
---
type: command
name: deleteMacro
suite: Keyboard Maestro Suite
---
```

## Command: deleteMacro

**Description:** Delete macro

### Direct Parameter
- **Description:** The UID or unique name of the macro to delete
- **Types:** text
<a name="deletemacrogroup"></a>
```yaml
---
type: command
name: deleteMacroGroup
suite: Keyboard Maestro Suite
---
```

## Command: deleteMacroGroup

**Description:** Delete macro group

### Direct Parameter
- **Description:** The UID or unique name of the macro group to delete
- **Types:** text
<a name="reload"></a>
```yaml
---
type: command
name: reload
suite: Keyboard Maestro Suite
---
```

## Command: reload

**Description:** Reload macros.

<a name="show_preference_pane"></a>
```yaml
---
type: command
name: show preference pane
suite: Keyboard Maestro Suite
---
```

## Command: show preference pane

**Description:** Show Preference Pane

### Direct Parameter
- **Description:** The name of the Keyboard Maestro preference pane to display
- **Types:** text
<a name="application"></a>
```yaml
---
type: class
name: application
suite: Keyboard Maestro Suite
---
```

## Class: application

**Description:** Keyboard Maestro application class.

**Inherits:** application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| global macro group | the global macro group | macro group | r |
| disabled group holder | the disabled macro group holder | disabled macro group holder | r |
| selected macro groups | the selected macro groups / smart groups in the macro editor | list of specifier | read/write |
| selected macros | the selected macros in the macro editor | list of specifier | read/write |

### Elements
- **Type:** macro group
- **Type:** smart group
- **Type:** macro
<a name="macro_group"></a>
```yaml
---
type: class
name: macro group
suite: Keyboard Maestro Suite
---
```

## Class: macro group

**Description:** A macro group.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| name | the macro group's name | text | rw |
| selected | is the macro group selected? | boolean | r |
| creation date | the date on which the macro group was created | date | r |
| modification date | the date on which the macro was modified | date | r |
| size | the approximate storage size of the macro group | integer | r |
| enabled | is the macro group enabled? | boolean | rw |
| disabled on this Mac | is the macro group disabled on this Mac? | boolean | rw |
| available application xml | the available application XML | text | rw |
| available window xml | the available window XML | text | rw |
| activation xml | the activation XML | text | rw |
| display in menu bar xml | the display in menu bar XML | text | rw |
| xml | the XML of the macro group and its contents | text | r |
| group xml | the XML of just the macro group | text | r |

### Elements
- **Type:** macro
### Responds To
- **Command:** select
- **Command:** edit
<a name="smart_group"></a>
```yaml
---
type: class
name: smart group
suite: Keyboard Maestro Suite
---
```

## Class: smart group

**Description:** A smart group.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| selected | is the smart group selected? | boolean | r |
| name | the smart group's name | text | rw |
| creation date | the date on which the smart group was created. | date | r |
| modification date | the date on which the macro was modified | date | r |
| search strings | The search strings | list of text | rw |
| xml | the XML of the smart group | text | r |

### Responds To
- **Command:** select
- **Command:** edit
<a name="disabled_macro_group_holder"></a>
```yaml
---
type: class
name: disabled macro group holder
suite: Keyboard Maestro Suite
---
```

## Class: disabled macro group holder

**Description:** The disabled macro group holder

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| name | the disabled macro group holder's name | text | r |
| selected | is the disabled macro group holder selected? | boolean | r |

### Responds To
- **Command:** select
<a name="macro"></a>
```yaml
---
type: class
name: macro
suite: Keyboard Maestro Suite
---
```

## Class: macro

**Description:** A macro.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| selected | is the macro selected? | boolean | r |
| name | the macro's name | text | rw |
| macro group | the containing macro group | macro group | r |
| enabled | is the macro enabled? | boolean | rw |
| creation date | the date on which the macro was created | date | r |
| modification date | the date on which the macro was modified | date | r |
| used date | the date on which the macro was used | date | r |
| size | the approximate storage size of the macro | integer | r |
| xml | the XML of the macro | text | r |

### Elements
- **Type:** trigger
- **Type:** action
### Responds To
- **Command:** select
- **Command:** edit
<a name="trigger"></a>
```yaml
---
type: class
name: trigger
suite: Keyboard Maestro Suite
---
```

## Class: trigger

**Description:** A trigger

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| description | the trigger's description | text | r |
| xml | the trigger XML | text | rw |

<a name="action"></a>
```yaml
---
type: class
name: action
suite: Keyboard Maestro Suite
---
```

## Class: action

**Description:** An action

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| name | the action's name | text | rw |
| enabled | is the action enabled? | boolean | rw |
| xml | the action XML | text | rw |
| disclosed | is the action disclosed? | boolean | rw |
| timeout period | the action's timeout period | real | rw |
| timeout aborts | does the action abort the macro on timeout | boolean | rw |
| timeout notifies | does the action notify on timeout | boolean | rw |
| failure aborts | does the action abort the macro on failure | boolean | rw |
| failure notifies | does the action notify on failure | boolean | rw |
| notes | the action's notes | text | rw |
| color | the action's color | text | rw |
| thenactions | the then actions | action list | r |
| thenactions disclosed | are the thenactions disclosed? | boolean | rw |
| elseactions | the else actions | action list | r |
| elseactions disclosed | are the elseactions disclosed? | boolean | rw |
| tryactions | the try actions | action list | r |
| tryactions disclosed | are the tryactions disclosed? | boolean | rw |
| catchactions | the catch actions | action list | r |
| catchactions disclosed | are the catchactions disclosed? | boolean | rw |
| actions disclosed | are the actions disclosed? | boolean | rw |

### Elements
- **Type:** action
- **Type:** case entry
### Responds To
- **Command:** select
<a name="case_entry"></a>
```yaml
---
type: class
name: case entry
suite: Keyboard Maestro Suite
---
```

## Class: case entry

**Description:** A case entry

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| xml | the case entry XML | text | rw |
| actions disclosed | are the actions disclosed? | boolean | rw |

### Elements
- **Type:** action
<a name="action_list"></a>
```yaml
---
type: class
name: action list
suite: Keyboard Maestro Suite
---
```

## Class: action list

**Description:** An action list

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier. | text | r |
| xml | the action list XML | text | rw |

### Elements
- **Type:** action
## Standard URL Suite

**Description:** The standard URL suite.

<a name="geturl"></a>
```yaml
---
type: command
name: geturl
suite: Standard URL Suite
---
```

## Command: geturl

**Description:** Handled the registration URL.

### Direct Parameter
- **Description:** the registration URL.
- **Types:** text
