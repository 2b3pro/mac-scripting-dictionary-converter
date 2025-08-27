# JSON Helper: AppleScript/JSX

## Table of Contents

### JSON commands
#### Commands
- [make JSON from](#make_json_from)
- [read JSON from](#read_json_from)
- [fetch JSON from](#fetch_json_from)
- [post as JSON](#post_as_json)


## JSON commands

**Description:** Terminology for JSON reading and writing.

<a name="make_json_from"></a>
```yaml
---
type: command
name: make JSON from
suite: JSON commands
---
```

## Command: make JSON from

**Description:** returns a JSON string from an AppleScript record or list, or an empty string if the operation fails

### Direct Parameter
- **Description:** an AppleScript record or list
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| pretty printing | should the human readable JSON be returned | boolean | Yes |

### Result
- **Description:** human readable JSON
- **Types:** text
<a name="read_json_from"></a>
```yaml
---
type: command
name: read JSON from
suite: JSON commands
---
```

## Command: read JSON from

**Description:** returns an AppleScript record or list from a JSON string, or an empty string if the operation fails

### Direct Parameter
- **Description:** a JSON formatted string
- **Types:** text
### Result
- **Description:** AppleScript record or list
- **Types:** any
<a name="fetch_json_from"></a>
```yaml
---
type: command
name: fetch JSON from
suite: JSON commands
---
```

## Command: fetch JSON from

**Description:** returns an AppleScript record or list from a url that returns JSON, or an empty string if the operation fails

### Direct Parameter
- **Description:** a url
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| cleaning feed | a boolean parameter requesting the json feed to be cleaned when fetching | boolean | Yes |
| name | a string with the user name for HTTP BASIC authentication | text | Yes |
| password | a string with the password for HTTP BASIC authentication | text | Yes |

### Result
- **Description:** AppleScript record or list
- **Types:** any
<a name="post_as_json"></a>
```yaml
---
type: command
name: post as JSON
suite: JSON commands
---
```

## Command: post as JSON

### Direct Parameter
- **Description:** The list, record or string to be converted to JSON and posted
- **Types:** any
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to URL | the URL to post to | text | No |
| name | a string with the user name for HTTP BASIC authentication | text | Yes |
| password | a string with the password for HTTP BASIC authentication | text | Yes |

### Result
- **Description:** the API response
- **Types:** any
