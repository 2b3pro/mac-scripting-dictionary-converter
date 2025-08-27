# Alfred: AppleScript/JSX

## Table of Contents

### Alfred Suite
#### Commands
- [search](#search)
- [action](#action)
- [browse](#browse)
- [run trigger](#run_trigger)
- [reload workflow](#reload_workflow)
- [reveal workflow](#reveal_workflow)
- [set configuration](#set_configuration)
- [remove configuration](#remove_configuration)
- [set theme](#set_theme)


## Alfred Suite

**Description:** Alfred Scripts

<a name="search"></a>
```yaml
---
type: command
name: search
suite: Alfred Suite
---
```

## Command: search

**Description:** Show Alfred with the given text

### Direct Parameter
- **Description:** The search string to populate Alfred with
- **Types:** text
<a name="action"></a>
```yaml
---
type: command
name: action
suite: Alfred Suite
---
```

## Command: action

**Description:** Show Alfred actions for the given file

### Direct Parameter
- **Description:** The items to show actions for
- **Types:** list of text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| as type | An optional type for the items; file, url or text | text | Yes |

<a name="browse"></a>
```yaml
---
type: command
name: browse
suite: Alfred Suite
---
```

## Command: browse

**Description:** Show Alfred file system navigation for given path

### Direct Parameter
- **Description:** The path or search string to browse
- **Types:** text
<a name="run_trigger"></a>
```yaml
---
type: command
name: run trigger
suite: Alfred Suite
---
```

## Command: run trigger

**Description:** Run Alfred workflow trigger

### Direct Parameter
- **Description:** The identifier of the trigger
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in workflow | The workflow bundle identifer | text | No |
| with argument | An optional argument | text | Yes |

<a name="reload_workflow"></a>
```yaml
---
type: command
name: reload workflow
suite: Alfred Suite
---
```

## Command: reload workflow

**Description:** Reload Workflow with given UID (folder name) or Bundle ID

### Direct Parameter
- **Description:** The UID (folder name), or the Bundle ID of the workflow to reload
- **Types:** text
<a name="reveal_workflow"></a>
```yaml
---
type: command
name: reveal workflow
suite: Alfred Suite
---
```

## Command: reveal workflow

**Description:** Reveal Workflow with given UID (folder name) or Bundle ID

### Direct Parameter
- **Description:** The UID (folder name), or the Bundle ID of the workflow to reveal
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| configuration | Optionally open the configuration for this workflow | boolean | Yes |

<a name="set_configuration"></a>
```yaml
---
type: command
name: set configuration
suite: Alfred Suite
---
```

## Command: set configuration

**Description:** Modify workflow configuration value, or set environment variable

### Direct Parameter
- **Description:** The name of the variable
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to value | The value to set | text | No |
| in workflow | The workflow bundle identifer | text | No |
| exportable | If this environment variable is fine for export, i.e. the Don't Export box is left unchecked (Defaults to Don't Export). This option is ignored for workflow configuration items | boolean | Yes |

<a name="remove_configuration"></a>
```yaml
---
type: command
name: remove configuration
suite: Alfred Suite
---
```

## Command: remove configuration

**Description:** Revert workflow configuration value to default, or delete environment variable

### Direct Parameter
- **Description:** The name of the variable
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in workflow | The workflow bundle identifer | text | No |

<a name="set_theme"></a>
```yaml
---
type: command
name: set theme
suite: Alfred Suite
---
```

## Command: set theme

**Description:** Change theme in Alfred

### Direct Parameter
- **Description:** The name of the theme to switch to
- **Types:** text
