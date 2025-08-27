# Apple Reminders: AppleScript/JSX

## Table of Contents

### Reminders Suite
#### Commands
- [show](#show)
#### Classs
- [account](#account)
- [list](#list)
- [reminder](#reminder)
#### Enumerations
- [saveable file format](#saveable_file_format)
#### Class Extensions
- [application](#application)


## Reminders Suite

**Description:** Terms and Events for controlling the Reminders application

<a name="show"></a>
```yaml
---
type: command
name: show
suite: Reminders Suite
---
```

## Command: show

**Description:** Show an object in the Reminders UI

### Direct Parameter
- **Description:** The object to be shown
- **Types:** list, reminder
### Result
- **Description:** The object shown
- **Types:** list, reminder
<a name="account"></a>
```yaml
---
type: class
name: account
suite: Reminders Suite
---
```

## Class: account

**Description:** An account in the Reminders application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the account | text | r |
| name | The name of the account | text | r |

### Elements
- **Type:** list
- **Type:** reminder
### Responds To
- **Command:** show
<a name="list"></a>
```yaml
---
type: class
name: list
suite: Reminders Suite
---
```

## Class: list

**Description:** A list in the Reminders application

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the list | text | r |
| name | The name of the list | text | read/write |
| container | The container of the list | account, list | r |
| color | The color of the list | text | read/write |
| emblem | The emblem icon name of the list | text | read/write |

### Elements
- **Type:** reminder
### Responds To
- **Command:** show
<a name="reminder"></a>
```yaml
---
type: class
name: reminder
suite: Reminders Suite
---
```

## Class: reminder

**Description:** A reminder in the Reminders application

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of the reminder | text | read/write |
| id | The unique identifier of the reminder | text | r |
| container | The container of the reminder | list, reminder | r |
| creation date | The creation date of the reminder | date | r |
| modification date | The modification date of the reminder | date | r |
| body | The notes attached to the reminder | text | read/write |
| completed | Whether the reminder is completed | boolean | read/write |
| completion date | The completion date of the reminder | date | read/write |
| due date | The due date of the reminder; will set both date and time | date | read/write |
| allday due date | The all-day due date of the reminder; will only set a date | date | read/write |
| remind me date | The remind date of the reminder | date | read/write |
| priority | The priority of the reminder; 0: no priority, 1–4: high, 5: medium, 6–9: low | integer | read/write |
| flagged | Whether the reminder is flagged | boolean | read/write |

### Responds To
- **Command:** show
<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: Reminders Suite
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| text | Text File Format |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Reminders Suite
---
```

## Class Extension: application

**Description:** The Reminders application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| default account | The default account in the Reminders application | account | r |
| default list | The default list in the Reminders application | list | r |

### Elements
- **Type:** account
- **Type:** list
- **Type:** reminder
