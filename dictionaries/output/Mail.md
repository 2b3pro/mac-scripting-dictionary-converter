# Mail Terminology: AppleScript/JSX

## Table of Contents

### Standard Suite
#### Commands
- [delete](#delete)
- [duplicate](#duplicate)
- [move](#move)
### Text Suite
#### Classs
- [rich text](#rich_text)
- [attachment](#attachment)
- [paragraph](#paragraph)
- [word](#word)
- [character](#character)
- [attribute run](#attribute_run)
#### Value Types
- [RGB color](#rgb_color)
### Mail
#### Commands
- [bounce](#bounce)
- [check for new mail](#check_for_new_mail)
- [extract name from](#extract_name_from)
- [extract address from](#extract_address_from)
- [forward](#forward)
- [GetURL](#geturl)
- [import Mail mailbox](#import_mail_mailbox)
- [mailto](#mailto)
- [perform mail action with messages](#perform_mail_action_with_messages)
- [redirect](#redirect)
- [reply](#reply)
- [send](#send)
- [synchronize](#synchronize)
#### Classs
- [outgoing message](#outgoing_message)
- [ldap server](#ldap_server)
- [OLD message editor](#old_message_editor)
- [message viewer](#message_viewer)
- [signature](#signature)
#### Enumerations
- [saveable file format](#saveable_file_format)
- [DefaultMessageFormat](#defaultmessageformat)
- [HeaderDetail](#headerdetail)
- [LdapScope](#ldapscope)
- [QuotingColor](#quotingcolor)
- [ViewerColumns](#viewercolumns)
#### Class Extensions
- [application](#application)
### Mail Framework
#### Classs
- [message](#message)
- [account](#account)
- [imap account](#imap_account)
- [iCloud account](#icloud_account)
- [pop account](#pop_account)
- [smtp server](#smtp_server)
- [mailbox](#mailbox)
- [rule](#rule)
- [rule condition](#rule_condition)
- [recipient](#recipient)
- [bcc recipient](#bcc_recipient)
- [cc recipient](#cc_recipient)
- [to recipient](#to_recipient)
- [container](#container)
- [header](#header)
- [mail attachment](#mail_attachment)
#### Enumerations
- [Authentication](#authentication)
- [HighlightColors](#highlightcolors)
- [MessageCachingPolicy](#messagecachingpolicy)
- [RuleQualifier](#rulequalifier)
- [RuleType](#ruletype)
- [TypeOfAccount](#typeofaccount)


## Standard Suite

**Description:** Common classes and commands for all applications.

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
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The location for the new copy or copies. | location specifier | Yes |
| with properties | Properties to set in the new copy or copies right away. | record | Yes |

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
- **Types:** specifier
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The new location for the object(s). | location specifier | No |

## Text Suite

**Description:** A set of basic classes for text processing.

<a name="rich_text"></a>
```yaml
---
type: class
name: rich text
suite: Text Suite
---
```

## Class: rich text

**Description:** Rich (styled) text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | RGB color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | number | read/write |

### Elements
- **Type:** paragraph
- **Type:** word
- **Type:** character
- **Type:** attribute run
- **Type:** attachment
<a name="attachment"></a>
```yaml
---
type: class
name: attachment
suite: Text Suite
---
```

## Class: attachment

**Description:** Represents an inline text attachment. This class is used mainly for make commands.

**Inherits:** rich text

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| file name | The file for the attachment | file | read/write |

<a name="paragraph"></a>
```yaml
---
type: class
name: paragraph
suite: Text Suite
---
```

## Class: paragraph

**Description:** This subdivides the text into paragraphs.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | RGB color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | number | read/write |

### Elements
- **Type:** word
- **Type:** character
- **Type:** attribute run
- **Type:** attachment
<a name="word"></a>
```yaml
---
type: class
name: word
suite: Text Suite
---
```

## Class: word

**Description:** This subdivides the text into words.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | RGB color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | number | read/write |

### Elements
- **Type:** character
- **Type:** attribute run
- **Type:** attachment
<a name="character"></a>
```yaml
---
type: class
name: character
suite: Text Suite
---
```

## Class: character

**Description:** This subdivides the text into characters.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the character. | RGB color | read/write |
| font | The name of the font of the character. | text | read/write |
| size | The size in points of the character. | number | read/write |

### Elements
- **Type:** attribute run
- **Type:** attachment
<a name="attribute_run"></a>
```yaml
---
type: class
name: attribute run
suite: Text Suite
---
```

## Class: attribute run

**Description:** This subdivides the text into chunks that all have the same attributes.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color | The color of the first character. | RGB color | read/write |
| font | The name of the font of the first character. | text | read/write |
| size | The size in points of the first character. | number | read/write |

### Elements
- **Type:** paragraph
- **Type:** word
- **Type:** character
- **Type:** attachment
<a name="rgb_color"></a>
```yaml
---
type: value-type
name: RGB color
suite: Text Suite
---
```

## Value Type: RGB color

## Mail

**Description:** Classes and commands for the Mail application

<a name="bounce"></a>
```yaml
---
type: command
name: bounce
suite: Mail
---
```

## Command: bounce

**Description:** Does nothing at all (deprecated)

### Direct Parameter
- **Description:** the message to bounce
- **Types:** message
<a name="check_for_new_mail"></a>
```yaml
---
type: command
name: check for new mail
suite: Mail
---
```

## Command: check for new mail

**Description:** Triggers a check for email.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| for | Specify the account that you wish to check for mail | account | Yes |

<a name="extract_name_from"></a>
```yaml
---
type: command
name: extract name from
suite: Mail
---
```

## Command: extract name from

**Description:** Command to get the full name out of a fully specified email address. E.g. Calling this with "John Doe <jdoe@example.com>" as the direct object would return "John Doe"

### Direct Parameter
- **Description:** fully formatted email address
- **Types:** text
### Result
- **Description:** the full name
- **Types:** text
<a name="extract_address_from"></a>
```yaml
---
type: command
name: extract address from
suite: Mail
---
```

## Command: extract address from

**Description:** Command to get just the email address of a fully specified email address. E.g. Calling this with "John Doe <jdoe@example.com>" as the direct object would return "jdoe@example.com"

### Direct Parameter
- **Description:** fully formatted email address
- **Types:** text
### Result
- **Description:** the email address
- **Types:** text
<a name="forward"></a>
```yaml
---
type: command
name: forward
suite: Mail
---
```

## Command: forward

**Description:** Creates a forwarded message.

### Direct Parameter
- **Description:** the message to forward
- **Types:** message
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| opening window | Whether the window for the forwarded message is shown. Default is to not show the window. | boolean | Yes |

### Result
- **Description:** the message to be forwarded
- **Types:** outgoing message
<a name="geturl"></a>
```yaml
---
type: command
name: GetURL
suite: Mail
---
```

## Command: GetURL

**Description:** Opens a mailto URL.

### Direct Parameter
- **Description:** the mailto URL
- **Types:** text
<a name="import_mail_mailbox"></a>
```yaml
---
type: command
name: import Mail mailbox
suite: Mail
---
```

## Command: import Mail mailbox

**Description:** Imports a mailbox created by Mail.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| at | the mailbox or folder of mailboxes to import | file | No |

<a name="mailto"></a>
```yaml
---
type: command
name: mailto
suite: Mail
---
```

## Command: mailto

**Description:** Opens a mailto URL.

### Direct Parameter
- **Description:** the mailto URL
- **Types:** text
<a name="perform_mail_action_with_messages"></a>
```yaml
---
type: command
name: perform mail action with messages
suite: Mail
---
```

## Command: perform mail action with messages

**Description:** Script handler invoked by rules and menus that execute AppleScripts. The direct parameter of this handler is a list of messages being acted upon.

### Direct Parameter
- **Description:** the message being acted upon
- **Types:** message
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in mailboxes | If the script is being executed by the user selecting an item in the scripts menu, this argument will specify the mailboxes that are currently selected. Otherwise it will not be specified. | mailbox | Yes |
| for rule | If the script is being executed by a rule action, this argument will be the rule being invoked. Otherwise it will not be specified. | rule | Yes |

<a name="redirect"></a>
```yaml
---
type: command
name: redirect
suite: Mail
---
```

## Command: redirect

**Description:** Creates a redirected message.

### Direct Parameter
- **Description:** the message to redirect
- **Types:** message
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| opening window | Whether the window for the redirected message is shown. Default is to not show the window. | boolean | Yes |

### Result
- **Description:** the redirected message
- **Types:** outgoing message
<a name="reply"></a>
```yaml
---
type: command
name: reply
suite: Mail
---
```

## Command: reply

**Description:** Creates a reply message.

### Direct Parameter
- **Description:** the message to reply to
- **Types:** message
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| opening window | Whether the window for the reply message is shown. Default is to not show the window. | boolean | Yes |
| reply to all | Whether to reply to all recipients. Default is to reply to the sender only. | boolean | Yes |

### Result
- **Description:** the reply message
- **Types:** outgoing message
<a name="send"></a>
```yaml
---
type: command
name: send
suite: Mail
---
```

## Command: send

**Description:** Sends a message.

### Direct Parameter
- **Description:** the message to send
- **Types:** outgoing message
### Result
- **Description:** true if sending was successful, false if not
- **Types:** boolean
<a name="synchronize"></a>
```yaml
---
type: command
name: synchronize
suite: Mail
---
```

## Command: synchronize

**Description:** Command to trigger synchronizing of an IMAP account with the server.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with | The account to synchronize | account | No |

<a name="outgoing_message"></a>
```yaml
---
type: class
name: outgoing message
suite: Mail
---
```

## Class: outgoing message

**Description:** A new email message

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| sender | The sender of the message | text | read/write |
| subject | The subject of the message | text | read/write |
| visible | Controls whether the message window is shown on the screen. The default is false | boolean | read/write |
| message signature | The signature of the message | signature, missing value | read/write |
| id | The unique identifier of the message | integer | r |
| html content | Does nothing at all (deprecated) | text | w |
| vcard path | Does nothing at all (deprecated) | file | w |

### Elements
- **Type:** bcc recipient
- **Type:** cc recipient
- **Type:** recipient
- **Type:** to recipient
### Responds To
- **Command:** save
- **Command:** close
- **Command:** send
<a name="ldap_server"></a>
```yaml
---
type: class
name: ldap server
suite: Mail
---
```

## Class: ldap server

**Description:** DEPRECATED - DO NOT USE

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| enabled | Does nothing at all (deprecated) | boolean | read/write |
| name | Does nothing at all (deprecated) | text | read/write |
| port | Does nothing at all (deprecated) | integer | read/write |
| scope | Does nothing at all (deprecated) | LdapScope | read/write |
| search base | Does nothing at all (deprecated) | text | read/write |
| host name | Does nothing at all (deprecated) | text | read/write |

<a name="old_message_editor"></a>
```yaml
---
type: class
name: OLD message editor
suite: Mail
---
```

## Class: OLD message editor

**Description:** DEPRECATED - DO NOT USE

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| OLD compose message | DEPRECATED - DO NOT USE | outgoing message | read/write |

<a name="message_viewer"></a>
```yaml
---
type: class
name: message viewer
suite: Mail
---
```

## Class: message viewer

**Description:** Represents the object responsible for managing a viewer window

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| drafts mailbox | The top level Drafts mailbox | mailbox | r |
| inbox | The top level In mailbox | mailbox | r |
| junk mailbox | The top level Junk mailbox | mailbox | r |
| outbox | The top level Out mailbox | mailbox | r |
| sent mailbox | The top level Sent mailbox | mailbox | r |
| trash mailbox | The top level Trash mailbox | mailbox | r |
| sort column | The column that is currently sorted in the viewer | ViewerColumns | read/write |
| sorted ascending | Whether the viewer is sorted ascending or not | boolean | read/write |
| mailbox list visible | Controls whether the list of mailboxes is visible or not | boolean | read/write |
| preview pane is visible | Controls whether the preview pane of the message viewer window is visible or not | boolean | read/write |
| visible columns | List of columns that are visible. The subject column and the message status column will always be visible | ViewerColumns | read/write |
| id | The unique identifier of the message viewer | integer | r |
| visible messages | List of messages currently being displayed in the viewer | message | read/write |
| selected messages | List of messages currently selected | message | read/write |
| selected mailboxes | List of mailboxes currently selected in the list of mailboxes | mailbox | read/write |

### Elements
- **Type:** message
<a name="signature"></a>
```yaml
---
type: class
name: signature
suite: Mail
---
```

## Class: signature

**Description:** Email signatures

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| content | Contents of email signature. If there is a version with fonts and/or styles, that will be returned over the plain text version | text | read/write |
| name | Name of the signature | text | read/write |

<a name="saveable_file_format"></a>
```yaml
---
type: enumeration
name: saveable file format
suite: Mail
---
```

## Enumeration: saveable file format

### Enumerators
| Name | Description |
|---|---|
| native format | Native format |

<a name="defaultmessageformat"></a>
```yaml
---
type: enumeration
name: DefaultMessageFormat
suite: Mail
---
```

## Enumeration: DefaultMessageFormat

### Enumerators
| Name | Description |
|---|---|
| plain format | Plain Text |
| rich format | Rich Text |

<a name="headerdetail"></a>
```yaml
---
type: enumeration
name: HeaderDetail
suite: Mail
---
```

## Enumeration: HeaderDetail

### Enumerators
| Name | Description |
|---|---|
| all | All |
| custom | Custom |
| default | Default |
| no headers | No headers |

<a name="ldapscope"></a>
```yaml
---
type: enumeration
name: LdapScope
suite: Mail
---
```

## Enumeration: LdapScope

### Enumerators
| Name | Description |
|---|---|
| base | LDAP scope of 'Base' |
| one level | LDAP scope of 'One Level' |
| subtree | LDAP scope of 'Subtree' |

<a name="quotingcolor"></a>
```yaml
---
type: enumeration
name: QuotingColor
suite: Mail
---
```

## Enumeration: QuotingColor

### Enumerators
| Name | Description |
|---|---|
| blue | Blue |
| green | Green |
| orange | Orange |
| other | Other |
| purple | Purple |
| red | Red |
| yellow | Yellow |

<a name="viewercolumns"></a>
```yaml
---
type: enumeration
name: ViewerColumns
suite: Mail
---
```

## Enumeration: ViewerColumns

### Enumerators
| Name | Description |
|---|---|
| attachments column | Column containing the number of attachments a message contains |
| message color | Used to indicate sorting should be done by color |
| date received column | Column containing the date a message was received |
| date sent column | Column containing the date a message was sent |
| flags column | Column containing the flags of a message |
| from column | Column containing the sender's name |
| mailbox column | Column containing the name of the mailbox or account a message is in |
| message status column | Column indicating a messages status (read, unread, replied to, forwarded, etc) |
| number column | Column containing the number of a message in a mailbox |
| size column | Column containing the size of a message |
| subject column | Column containing the subject of a message |
| to column | Column containing the recipients of a message |
| date last saved column | Column containing the date a draft message was saved |

<a name="application"></a>
```yaml
---
type: class-extension
name: application
suite: Mail
---
```

## Class Extension: application

**Description:** Mail's top level scripting object.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| always bcc myself | Indicates whether you will be included in the Bcc: field of messages which you are composing | boolean | read/write |
| always cc myself | Indicates whether you will be included in the Cc: field of messages which you are composing | boolean | read/write |
| selection | List of messages that the user has selected | message | r |
| application version | The build number of the application | text | r |
| fetch interval | The interval (in minutes) between automatic fetches of new mail, -1 means to use an automatically determined interval | integer | read/write |
| background activity count | Number of background activities currently running in Mail, according to the Activity window | integer | r |
| choose signature when composing | Indicates whether user can choose a signature directly in a new compose window | boolean | read/write |
| color quoted text | Indicates whether quoted text should be colored | boolean | read/write |
| default message format | Default format for messages being composed or message replies | DefaultMessageFormat | read/write |
| download html attachments | Indicates whether images and attachments in HTML messages should be downloaded and displayed | boolean | read/write |
| drafts mailbox | The top level Drafts mailbox | mailbox | r |
| expand group addresses | Indicates whether group addresses will be expanded when entered into the address fields of a new compose message | boolean | read/write |
| fixed width font | Font for plain text messages, only used if 'use fixed width font' is set to true | text | read/write |
| fixed width font size | Font size for plain text messages, only used if 'use fixed width font' is set to true | real | read/write |
| framework version | Returns the same thing as application version (deprecated) | text | r |
| header detail | This always returns default, and setting it doesn't do anything (deprecated) | HeaderDetail | read/write |
| inbox | The top level In mailbox | mailbox | r |
| include all original message text | Indicates whether all of the original message will be quoted or only the text you have selected (if any) | boolean | read/write |
| quote original message | Indicates whether the text of the original message will be included in replies | boolean | read/write |
| check spelling while typing | Indicates whether spelling will be checked automatically in messages being composed | boolean | read/write |
| junk mailbox | The top level Junk mailbox | mailbox | r |
| level one quoting color | Color for quoted text with one level of indentation | QuotingColor | read/write |
| level two quoting color | Color for quoted text with two levels of indentation | QuotingColor | read/write |
| level three quoting color | Color for quoted text with three levels of indentation | QuotingColor | read/write |
| message font | Font for messages (proportional font) | text | read/write |
| message font size | Font size for messages (proportional font) | real | read/write |
| message list font | Font for message list | text | read/write |
| message list font size | Font size for message list | real | read/write |
| new mail sound | Name of new mail sound or 'None' if no sound is selected | text | read/write |
| outbox | The top level Out mailbox | mailbox | r |
| should play other mail sounds | Indicates whether sounds will be played for various things such as when a messages is sent or if no mail is found when manually checking for new mail or if there is a fetch error | boolean | read/write |
| same reply format | Indicates whether replies will be in the same text format as the message to which you are replying | boolean | read/write |
| selected signature | Name of current selected signature (or 'randomly', 'sequentially', or 'none') | text | read/write |
| sent mailbox | The top level Sent mailbox | mailbox | r |
| fetches automatically | Indicates whether mail will automatically be fetched at a specific interval | boolean | read/write |
| highlight selected conversation | Indicates whether messages in conversations should be highlighted in the Mail viewer window when not grouped | boolean | read/write |
| trash mailbox | The top level Trash mailbox | mailbox | r |
| use address completion | This always returns true, and setting it doesn't do anything (deprecated) | boolean | read/write |
| use fixed width font | Should fixed-width font be used for plain text messages? | boolean | read/write |
| primary email | The user's primary email address | text | r |
| hosts to log activity on | Indicates whether to log socket activity for the specified hosts | text | read/write |
| ports to log activity on | Indicates whether to log socket activity for the specified ports | integer | read/write |
| log all socket activity | Indicates whether all socket activity will be logged | boolean | read/write |
| memory statistics |  | record | r |
| use keychain | Ignored - Mail always uses the Keychain to store passwords | boolean | read/write |

### Elements
- **Type:** account
- **Type:** pop account
- **Type:** imap account
- **Type:** iCloud account
- **Type:** smtp server
- **Type:** outgoing message
- **Type:** ldap server
- **Type:** mailbox
- **Type:** OLD message editor
- **Type:** message viewer
- **Type:** rule
- **Type:** signature
### Responds To
- **Command:** check for new mail
- **Command:** import Mail mailbox
- **Command:** synchronize
## Mail Framework

**Description:** Classes and commands for the Mail framework

<a name="message"></a>
```yaml
---
type: class
name: message
suite: Mail Framework
---
```

## Class: message

**Description:** An email message

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| id | The unique identifier of the message. | integer | r |
| all headers | All the headers of the message | text | r |
| background color | The background color of the message | HighlightColors | read/write |
| mailbox | The mailbox in which this message is filed | mailbox | read/write |
| content | Contents of an email message | rich text | r |
| date received | The date a message was received | date | r |
| date sent | The date a message was sent | date | r |
| deleted status | Indicates whether the message is deleted or not | boolean | read/write |
| flagged status | Indicates whether the message is flagged or not | boolean | read/write |
| flag index | The flag on the message, or -1 if the message is not flagged | integer | read/write |
| junk mail status | Indicates whether the message has been marked junk or evaluated to be junk by the junk mail filter. | boolean | read/write |
| read status | Indicates whether the message is read or not | boolean | read/write |
| message id | The unique message ID string | text | r |
| source | Raw source of the message | text | r |
| reply to | The address that replies should be sent to | text | r |
| message size | The size (in bytes) of a message | integer | r |
| sender | The sender of the message | text | r |
| subject | The subject of the message | text | r |
| was forwarded | Indicates whether the message was forwarded or not | boolean | r |
| was redirected | Indicates whether the message was redirected or not | boolean | r |
| was replied to | Indicates whether the message was replied to or not | boolean | r |

### Elements
- **Type:** bcc recipient
- **Type:** cc recipient
- **Type:** recipient
- **Type:** to recipient
- **Type:** header
- **Type:** mail attachment
### Responds To
- **Command:** open
- **Command:** bounce
- **Command:** forward
- **Command:** redirect
- **Command:** reply
<a name="account"></a>
```yaml
---
type: class
name: account
suite: Mail Framework
---
```

## Class: account

**Description:** A Mail account for receiving messages (POP/IMAP). To create a new receiving account, use the 'pop account', 'imap account', and 'iCloud account' objects

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| delivery account | The delivery account used when sending mail from this account | smtp server, missing value | read/write |
| name | The name of an account | text | read/write |
| id | The unique identifier of the account | text | r |
| password | Password for this account. Can be set, but not read via scripting | text | read/write |
| authentication | Preferred authentication scheme for account | Authentication | read/write |
| account type | The type of an account | TypeOfAccount | r |
| email addresses | The list of email addresses configured for an account | text | read/write |
| full name | The users full name configured for an account | text | read/write |
| empty junk messages frequency | Number of days before junk messages are deleted (0 = delete on quit, -1 = never delete) | integer | read/write |
| empty sent messages frequency | Does nothing at all (deprecated) | integer | read/write |
| empty trash frequency | Number of days before messages in the trash are permanently deleted (0 = delete on quit, -1 = never delete) | integer | read/write |
| empty junk messages on quit | Indicates whether the messages in the junk messages mailboxes will be deleted on quit | boolean | read/write |
| empty sent messages on quit | Does nothing at all (deprecated) | boolean | read/write |
| empty trash on quit | Indicates whether the messages in deleted messages mailboxes will be permanently deleted on quit | boolean | read/write |
| enabled | Indicates whether the account is enabled or not | boolean | read/write |
| user name | The user name used to connect to an account | text | read/write |
| account directory | The directory where the account stores things on disk | file | r |
| port | The port used to connect to an account | integer | read/write |
| server name | The host name used to connect to an account | text | read/write |
| include when getting new mail | Does nothing at all (deprecated) | boolean | read/write |
| move deleted messages to trash | Indicates whether messages that are deleted will be moved to the trash mailbox | boolean | read/write |
| uses ssl | Indicates whether SSL is enabled for this receiving account | boolean | read/write |

### Elements
- **Type:** mailbox
<a name="imap_account"></a>
```yaml
---
type: class
name: imap account
suite: Mail Framework
---
```

## Class: imap account

**Description:** An IMAP email account

**Inherits:** account

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| compact mailboxes when closing | Indicates whether an IMAP mailbox is automatically compacted when you quit Mail or switch to another mailbox | boolean | read/write |
| message caching | Message caching setting for this account | MessageCachingPolicy | read/write |
| store drafts on server | Indicates whether drafts will be stored on the IMAP server | boolean | read/write |
| store junk mail on server | Indicates whether junk mail will be stored on the IMAP server | boolean | read/write |
| store sent messages on server | Indicates whether sent messages will be stored on the IMAP server | boolean | read/write |
| store deleted messages on server | Indicates whether deleted messages will be stored on the IMAP server | boolean | read/write |

<a name="icloud_account"></a>
```yaml
---
type: class
name: iCloud account
suite: Mail Framework
---
```

## Class: iCloud account

**Description:** An iCloud or MobileMe email account

**Inherits:** imap account

<a name="pop_account"></a>
```yaml
---
type: class
name: pop account
suite: Mail Framework
---
```

## Class: pop account

**Description:** A POP email account

**Inherits:** account

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| big message warning size | If message size (in bytes) is over this amount, Mail will prompt you asking whether you want to download the message (-1 = do not prompt) | integer | read/write |
| delayed message deletion interval | Number of days before messages that have been downloaded will be deleted from the server (0 = delete immediately after downloading) | integer | read/write |
| delete mail on server | Indicates whether POP account deletes messages on the server after downloading | boolean | read/write |
| delete messages when moved from inbox | Indicates whether messages will be deleted from the server when moved from your POP inbox | boolean | read/write |

<a name="smtp_server"></a>
```yaml
---
type: class
name: smtp server
suite: Mail Framework
---
```

## Class: smtp server

**Description:** An SMTP account (for sending email)

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of an account | text | r |
| password | Password for this account. Can be set, but not read via scripting | text | read/write |
| account type | The type of an account | TypeOfAccount | r |
| authentication | Preferred authentication scheme for account | Authentication | read/write |
| enabled | Indicates whether the account is enabled or not | boolean | read/write |
| user name | The user name used to connect to an account | text | read/write |
| port | The port used to connect to an account | integer | read/write |
| server name | The host name used to connect to an account | text | read/write |
| uses ssl | Indicates whether SSL is enabled for this receiving account | boolean | read/write |

<a name="mailbox"></a>
```yaml
---
type: class
name: mailbox
suite: Mail Framework
---
```

## Class: mailbox

**Description:** A mailbox that holds messages

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | The name of a mailbox | text | read/write |
| unread count | The number of unread messages in the mailbox | integer | r |
| account |  | account | r |
| container |  | mailbox | r |

### Elements
- **Type:** mailbox
- **Type:** message
<a name="rule"></a>
```yaml
---
type: class
name: rule
suite: Mail Framework
---
```

## Class: rule

**Description:** Class for message rules

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| color message | If rule matches, apply this color | HighlightColors | read/write |
| delete message | If rule matches, delete message | boolean | read/write |
| forward text | If rule matches, prepend this text to the forwarded message. Set to empty string to include no prepended text | text | read/write |
| forward message | If rule matches, forward message to this address, or multiple addresses, separated by commas. Set to empty string to disable this action | text | read/write |
| mark flagged | If rule matches, mark message as flagged | boolean | read/write |
| mark flag index | If rule matches, mark message with the specified flag. Set to -1 to disable this action | integer | read/write |
| mark read | If rule matches, mark message as read | boolean | read/write |
| play sound | If rule matches, play this sound (specify name of sound or path to sound) | text | read/write |
| redirect message | If rule matches, redirect message to this address or multiple addresses, separate by commas. Set to empty string to disable this action | text | read/write |
| reply text | If rule matches, reply to message and prepend with this text. Set to empty string to disable this action | text | read/write |
| run script | If rule matches, run this compiled AppleScript file. Set to empty string to disable this action | file, missing value | read/write |
| all conditions must be met | Indicates whether all conditions must be met for rule to execute | boolean | read/write |
| copy message | If rule matches, copy to this mailbox | mailbox | read/write |
| move message | If rule matches, move to this mailbox | mailbox | read/write |
| highlight text using color | Indicates whether the color will be used to highlight the text or background of a message in the message list | boolean | read/write |
| enabled | Indicates whether the rule is enabled | boolean | read/write |
| name | Name of rule | text | read/write |
| should copy message | Indicates whether the rule has a copy action | boolean | read/write |
| should move message | Indicates whether the rule has a move action | boolean | read/write |
| stop evaluating rules | If rule matches, stop rule evaluation for this message | boolean | read/write |

### Elements
- **Type:** rule condition
<a name="rule_condition"></a>
```yaml
---
type: class
name: rule condition
suite: Mail Framework
---
```

## Class: rule condition

**Description:** Class for conditions that can be attached to a single rule

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| expression | Rule expression field | text | read/write |
| header | Rule header key | text | read/write |
| qualifier | Rule qualifier | RuleQualifier | read/write |
| rule type | Rule type | RuleType | read/write |

<a name="recipient"></a>
```yaml
---
type: class
name: recipient
suite: Mail Framework
---
```

## Class: recipient

**Description:** An email recipient

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| address | The recipients email address | text | read/write |
| name | The name used for display | text | read/write |

<a name="bcc_recipient"></a>
```yaml
---
type: class
name: bcc recipient
suite: Mail Framework
---
```

## Class: bcc recipient

**Description:** An email recipient in the Bcc: field

**Inherits:** recipient

<a name="cc_recipient"></a>
```yaml
---
type: class
name: cc recipient
suite: Mail Framework
---
```

## Class: cc recipient

**Description:** An email recipient in the Cc: field

**Inherits:** recipient

<a name="to_recipient"></a>
```yaml
---
type: class
name: to recipient
suite: Mail Framework
---
```

## Class: to recipient

**Description:** An email recipient in the To: field

**Inherits:** recipient

<a name="container"></a>
```yaml
---
type: class
name: container
suite: Mail Framework
---
```

## Class: container

**Description:** A mailbox that contains other mailboxes.

**Inherits:** mailbox

<a name="header"></a>
```yaml
---
type: class
name: header
suite: Mail Framework
---
```

## Class: header

**Description:** A header value for a message. E.g. To, Subject, From.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| content | Contents of the header | text | read/write |
| name | Name of the header value | text | read/write |

<a name="mail_attachment"></a>
```yaml
---
type: class
name: mail attachment
suite: Mail Framework
---
```

## Class: mail attachment

**Description:** A file attached to a received message.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| name | Name of the attachment | text | r |
| MIME type | MIME type of the attachment E.g. text/plain. | text | r |
| file size | Approximate size in bytes. | integer | r |
| downloaded | Indicates whether the attachment has been downloaded. | boolean | r |
| id | The unique identifier of the attachment. | text | r |

### Responds To
- **Command:** save
<a name="authentication"></a>
```yaml
---
type: enumeration
name: Authentication
suite: Mail Framework
---
```

## Enumeration: Authentication

### Enumerators
| Name | Description |
|---|---|
| password | Clear text password |
| apop | APOP |
| kerberos 5 | Kerberos V5 (GSSAPI) |
| ntlm | NTLM |
| md5 | CRAM-MD5 |
| external | External authentication (TLS client certificate) |
| Apple token | Apple token |
| none | None |

<a name="highlightcolors"></a>
```yaml
---
type: enumeration
name: HighlightColors
suite: Mail Framework
---
```

## Enumeration: HighlightColors

### Enumerators
| Name | Description |
|---|---|
| blue | Blue |
| gray | Gray |
| green | Green |
| none | None |
| orange | Orange |
| other | Other |
| purple | Purple |
| red | Red |
| yellow | Yellow |

<a name="messagecachingpolicy"></a>
```yaml
---
type: enumeration
name: MessageCachingPolicy
suite: Mail Framework
---
```

## Enumeration: MessageCachingPolicy

### Enumerators
| Name | Description |
|---|---|
| do not keep copies of any messages | Do not use this option (deprecated). If you do, Mail will use the 'all messages but omit attachments' policy |
| only messages I have read | Do not use this option (deprecated). If you do, Mail will use the 'all messages but omit attachments' policy |
| all messages but omit attachments | All messages but omit attachments |
| all messages and their attachments | All messages and their attachments |

<a name="rulequalifier"></a>
```yaml
---
type: enumeration
name: RuleQualifier
suite: Mail Framework
---
```

## Enumeration: RuleQualifier

### Enumerators
| Name | Description |
|---|---|
| begins with value | Begins with value |
| does contain value | Does contain value |
| does not contain value | Does not contain value |
| ends with value | Ends with value |
| equal to value | Equal to value |
| less than value | Less than value |
| greater than value | Greater than value |
| none | Indicates no qualifier is applicable |

<a name="ruletype"></a>
```yaml
---
type: enumeration
name: RuleType
suite: Mail Framework
---
```

## Enumeration: RuleType

### Enumerators
| Name | Description |
|---|---|
| account | Account |
| any recipient | Any recipient |
| cc header | Cc header |
| matches every message | Every message |
| from header | From header |
| header key | An arbitrary header key |
| message content | Message content |
| message is junk mail | Message is junk mail |
| sender is in my contacts | Sender is in my contacts |
| sender is in my previous recipients | Sender is in my previous recipients |
| sender is member of group | Sender is member of group |
| sender is not in my contacts | Sender is not in my contacts |
| sender is not in my previous recipients | sender is not in my previous recipients |
| sender is not member of group | Sender is not member of group |
| sender is VIP | Sender is VIP |
| subject header | Subject header |
| to header | To header |
| to or cc header | To or Cc header |
| attachment type | Attachment Type |

<a name="typeofaccount"></a>
```yaml
---
type: enumeration
name: TypeOfAccount
suite: Mail Framework
---
```

## Enumeration: TypeOfAccount

### Enumerators
| Name | Description |
|---|---|
| pop | POP |
| smtp | SMTP |
| imap | IMAP |
| iCloud | iCloud |
| unknown | Unknown |

