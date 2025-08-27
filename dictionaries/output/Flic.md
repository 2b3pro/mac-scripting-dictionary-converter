# Flic Terminology: AppleScript/JSX

## Table of Contents

### Flic Suite
#### Commands
- [execute task](#execute_task)
#### Classs
- [application](#application)


## Flic Suite

**Description:** Classes just for the Flic application.

<a name="execute_task"></a>
```yaml
---
type: command
name: execute task
suite: Flic Suite
---
```

## Command: execute task

**Description:** Executa a specific task.

### Direct Parameter
- **Description:** The UUID string of the task to execute.
- **Types:** text
<a name="application"></a>
```yaml
---
type: class
name: application
suite: Flic Suite
---
```

## Class: application

**Description:** Application object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| gettasks | Get a list of all available tasks | any | read/write |

