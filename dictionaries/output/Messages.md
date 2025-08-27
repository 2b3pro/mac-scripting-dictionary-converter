# Apple Messages: AppleScript/JSX

## Table of Contents

### Messages Suite
#### Commands
- [send](#send)
- [login](#login)
- [logout](#logout)
#### Classs
- [participant](#participant)
- [account](#account)
- [chat](#chat)
- [file transfer](#file_transfer)
#### Enumerations
- [service type](#service_type)
- [direction](#direction)
- [transfer status](#transfer_status)
- [connection status](#connection_status)
#### Class Extensions
- [application](#application)


## Messages Suite

**Description:** commands and classes for Messages scripting.

<a name="send"></a>
```yaml
---
type: command
name: send
suite: Messages Suite
---
```

## Command: send

**Description:** Sends a message to a participant or to a chat.

### Direct Parameter
- **Types:** file, text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to |  | participant, chat | No |

<a name="login"></a>
```yaml
---
type: command
name: login
suite: Messages Suite
---
```

## Command: login

**Description:** Login to all accounts.

<a name="logout"></a>
```yaml
---
type: command
name: logout
suite: Messages Suite
---
```

## Command: logout

**Description:** Logout of all accounts.

<a name="participant"></a>
```yaml
---
type: class
name: participant
suite: Messages Suite
---
```

## Class: participant

**Description:** A participant for an account.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The participant's unique identifier. For example: 01234567-89AB-CDEF-0123-456789ABCDEF:+11234567890 | text | r |
| account | The account for this participant. | account | r |
| name | The participant's name as it appears in the participant list. | text | r |
| handle | The participant's handle. | text | r |
| first name | The first name from this participan's Contacts card, if available | text | r |
| last name | The last name from this participant's Contacts card, if available | text | r |
| full name | The full name from this participant's Contacts card, if available | text | r |

<a name="account"></a>
```yaml
---
type: class
name: account
suite: Messages Suite
---
```

## Class: account

**Description:** An account that can be logged in to from this system

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | A unique identifier for this account. | text | r |
| description | The name of this account as defined in Account preferences description field | text | r |
| enabled | Is the account enabled? | boolean | read/write |
| connection status | The connection status for this account. | connection status | r |
| service type | The type of service for this account | service type | r |

### Elements
- **Type:** chat
- **Type:** participant
<a name="chat"></a>
```yaml
---
type: class
name: chat
suite: Messages Suite
---
```

## Class: chat

**Description:** An SMS or iMessage chat.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | A guid identifier for this chat. | text | r |
| name | The chat's name as it appears in the chat list. | text | r |
| account | The account which is participating in this chat. | account | r |

### Elements
- **Type:** participant
<a name="file_transfer"></a>
```yaml
---
type: class
name: file transfer
suite: Messages Suite
---
```

## Class: file transfer

**Description:** A file being sent or received

**Inherits:** item

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The guid for this file transfer | text | r |
| name | The name of this file | text | r |
| file path | The local path to this file transfer | file | r |
| direction | The direction in which this file is being sent | direction | r |
| account | The account on which this file transfer is taking place | account | r |
| participant | The other participatant in this file transfer | participant | r |
| file size | The total size in bytes of the completed file transfer | integer | r |
| file progress | The number of bytes that have been transferred | integer | r |
| transfer status | The current status of this file transfer | transfer status | r |
| started | The date that this file transfer started | date | r |

<a name="service_type"></a>
```yaml
---
type: enumeration
name: service type
suite: Messages Suite
---
```

## Enumeration: service type

### Enumerators
| Name | Description |
|---|---|
| SMS | None |
| iMessage | None |
| RCS | None |

<a name="direction"></a>
```yaml
---
type: enumeration
name: direction
suite: Messages Suite
---
```

## Enumeration: direction

### Enumerators
| Name | Description |
|---|---|
| incoming | None |
| outgoing | None |

<a name="transfer_status"></a>
```yaml
---
type: enumeration
name: transfer status
suite: Messages Suite
---
```

## Enumeration: transfer status

### Enumerators
| Name | Description |
|---|---|
| preparing | None |
| waiting | None |
| transferring | None |
| finalizing | None |
| finished | None |
| failed | None |

<a name="connection_status"></a>
```yaml
---
type: enumeration
name: connection status
suite: Messages Suite
---
```

## Enumeration: connection status

### Enumerators
| Name | Description |
|---|---|
| disconnecting | None |
| connected | None |
| connecting | None |
| disconnected | None |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Messages Suite
---
```

## Class Extension: application

**Description:** Messages application.

### Elements
- **Type:** participant
- **Type:** account
- **Type:** file transfer
- **Type:** chat
