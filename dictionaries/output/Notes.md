# Apple Notes: AppleScript/JSX

## Table of Contents

### Notes Suite
#### Commands
- [open note location](#open_note_location)
- [show](#show)
#### Classs
- [account](#account)
- [folder](#folder)
- [note](#note)
- [attachment](#attachment)
#### Enumerations
- [saveable file format](#saveable_file_format)
#### Class Extensions
- [application](#application)


## Notes Suite

**Description:** Terms and Events for controlling the Notes application

<a name="open_note_location"></a>
```yaml
---
type: command
name: open note location
suite: Notes Suite
---
```

## Command: open note location

**Description:** Open a note URL.

### Direct Parameter
- **Description:** The URL to be opened.
- **Types:** text
<a name="show"></a>
```yaml
---
type: command
name: show
suite: Notes Suite
---
```

## Command: show

**Description:** Show an object in the UI

### Direct Parameter
- **Description:** The object to be shown
- **Types:** account, folder, note, attachment
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| separately |  | boolean | Yes |

### Result
- **Description:** The object shown.
- **Types:** account, folder, note, attachment
<a name="account"></a>
```yaml
---
type: class
name: account
suite: Notes Suite
---
```

## Class: account

**Description:** a Notes account

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| default folder | the default folder for creating notes | folder | read/write |
| name | the name of the account | text | read/write |
| upgraded | Is the account upgraded? | boolean | r |
| id | the unique identifier of the account | text | r |

### Elements
- **Type:** folder
- **Type:** note
### Responds To
- **Command:** show
<a name="folder"></a>
```yaml
---
type: class
name: folder
suite: Notes Suite
---
```

## Class: folder

**Description:** a folder containing notes

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the folder | text | read/write |
| id | the unique identifier of the folder | text | r |
| shared | Is the folder shared? | boolean | r |
| container | the container of the folder | account, folder | r |

### Elements
- **Type:** folder
- **Type:** note
### Responds To
- **Command:** show
<a name="note"></a>
```yaml
---
type: class
name: note
suite: Notes Suite
---
```

## Class: note

**Description:** a note in the Notes application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the note (normally the first line of the body) | text | read/write |
| id | the unique identifier of the note | text | r |
| container | the folder of the note | folder | r |
| body | the HTML content of the note | text | read/write |
| plaintext | the plaintext content of the note | text | r |
| creation date | the creation date of the note | date | r |
| modification date | the modification date of the note | date | r |
| password protected | Is the note password protected? | boolean | r |
| shared | Is the note shared? | boolean | r |

### Elements
- **Type:** attachment
### Responds To
- **Command:** show
<a name="attachment"></a>
```yaml
---
type: class
name: attachment
suite: Notes Suite
---
```

## Class: attachment

**Description:** an attachment in a note

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | the name of the attachment | text | r |
| id | the unique identifier of the attachment | text | r |
| container | the note containing the attachment | note | r |
| content identifier | the content-id URL in the note's HTML | text | r |
| creation date | the creation date of the attachment | date | r |
| modification date | the modification date of the attachment | date | r |
| URL | for URL attachments, the URL the attachment represents | text | r |
| shared | Is the attachment shared? | boolean | r |

### Responds To
- **Command:** show
- **Command:** save
<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: Notes Suite
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| native format | Native format |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Notes Suite
---
```

## Class Extension: application

**Description:** the Notes application

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| default account | the default account for creating notes | account | read/write |
| selection | the selected note(s) | note | read/write |

### Elements
- **Type:** account
- **Type:** folder
- **Type:** note
- **Type:** attachment
