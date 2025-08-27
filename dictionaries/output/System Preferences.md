# System Preferences: AppleScript/JSX

## Table of Contents

### Standard Suite
### System Settings
#### Commands
- [reveal](#reveal)
- [authorize](#authorize)
- [timedLoad](#timedload)
#### Classs
- [pane](#pane)
- [anchor](#anchor)
#### Class Extensions
- [application](#application)


## Standard Suite

**Description:** None

## System Settings

**Description:** Classes and Commands specific to System Settings

<a name="reveal"></a>
```yaml
---
type: command
name: reveal
suite: System Settings
---
```

## Command: reveal

**Description:** Reveals a settings pane or an anchor within a pane.

### Direct Parameter
- **Types:** pane, anchor
### Result
- **Types:** pane, anchor
<a name="authorize"></a>
```yaml
---
type: command
name: authorize
suite: System Settings
---
```

## Command: authorize

**Description:** Prompt for authorization for a settings pane. Deprecated: no longer does anything.

### Direct Parameter
- **Types:** pane
### Result
- **Types:** pane
<a name="timedload"></a>
```yaml
---
type: command
name: timedLoad
suite: System Settings
---
```

## Command: timedLoad

**Description:** Times and loads given settings pane and returns load time. Deprecated: no longer does anything.

### Direct Parameter
- **Types:** pane
### Result
- **Types:** real
<a name="pane"></a>
```yaml
---
type: class
name: pane
suite: System Settings
---
```

## Class: pane

**Description:** A settings pane.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The id of the settings pane. | text | r |
| name | The name of the settings pane. | text | r |

### Elements
- **Type:** anchor
### Responds To
- **Command:** reveal
- **Command:** authorize
<a name="anchor"></a>
```yaml
---
type: class
name: anchor
suite: System Settings
---
```

## Class: anchor

**Description:** An anchor within a settings pane.

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the anchor. | text | r |

### Responds To
- **Command:** reveal
<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: System Settings
---
```

## Class Extension: application

**Description:** The System Settings top-level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| current pane | The currently selected pane. | pane | read/write |
| settings window | The main settings window. | window | r |
| show all | Is System Settings in show-all view? (Setting to false does nothing.) Deprecated: setting this property no longer does anything; it is always set to true. | boolean | read/write |

### Elements
- **Type:** pane
