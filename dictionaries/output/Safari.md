# Apple Safari: AppleScript/JSX

## Table of Contents

### Safari suite
#### Commands
- [add reading list item](#add_reading_list_item)
- [do JavaScript](#do_javascript)
- [email contents](#email_contents)
- [search the web](#search_the_web)
- [show bookmarks](#show_bookmarks)
- [show extensions preferences](#show_extensions_preferences)
- [dispatch message to extension](#dispatch_message_to_extension)
- [sync all plist to disk](#sync_all_plist_to_disk)
- [show privacy report](#show_privacy_report)
- [show credit card settings](#show_credit_card_settings)
#### Classs
- [tab](#tab)
- [sourceProvider](#sourceprovider)
- [contentsProvider](#contentsprovider)
#### Class Extensions
- [window](#window)
- [document](#document)


## Safari suite

**Description:** Safari specific classes

<a name="add_reading_list_item"></a>
```yaml
---
type: command
name: add reading list item
suite: Safari suite
---
```

## Command: add reading list item

**Description:** Add a new Reading List item with the given URL. Allows a custom title and preview text to be specified.

### Direct Parameter
- **Description:** URL of the Reading List item
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| and preview text | Preview text for the Reading List item, usually the first few sentences of the article | text | Yes |
| with title | Title of the Reading List item | text | Yes |

<a name="do_javascript"></a>
```yaml
---
type: command
name: do JavaScript
suite: Safari suite
---
```

## Command: do JavaScript

**Description:** Applies a string of JavaScript code to a document.

### Direct Parameter
- **Description:** The JavaScript code to evaluate.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The tab that the JavaScript should be evaluated in. | document, tab | Yes |

### Result
- **Types:** any
<a name="email_contents"></a>
```yaml
---
type: command
name: email contents
suite: Safari suite
---
```

## Command: email contents

**Description:** Emails the contents of a tab.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| of | The tab to send. | tab, document | Yes |

<a name="search_the_web"></a>
```yaml
---
type: command
name: search the web
suite: Safari suite
---
```

## Command: search the web

**Description:** Searches the web using Safari's current search provider.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The tab that the search results should shown in. | document, tab | Yes |
| for | The query to search for. | text | No |

<a name="show_bookmarks"></a>
```yaml
---
type: command
name: show bookmarks
suite: Safari suite
---
```

## Command: show bookmarks

**Description:** Shows Safari's bookmarks.

<a name="show_extensions_preferences"></a>
```yaml
---
type: command
name: show extensions preferences
suite: Safari suite
---
```

## Command: show extensions preferences

**Description:** Show Safari Extensions preferences.

### Direct Parameter
- **Description:** The identifier of the extension to select.
- **Types:** text
<a name="dispatch_message_to_extension"></a>
```yaml
---
type: command
name: dispatch message to extension
suite: Safari suite
---
```

## Command: dispatch message to extension

**Description:** Dispatch a message to a Safari Extension.

### Direct Parameter
- **Description:** A dictionary describing the message
- **Types:** any
<a name="sync_all_plist_to_disk"></a>
```yaml
---
type: command
name: sync all plist to disk
suite: Safari suite
---
```

## Command: sync all plist to disk

**Description:** Make sure that all in-memory structures are in-sync with their on-disk counterparts.

<a name="show_privacy_report"></a>
```yaml
---
type: command
name: show privacy report
suite: Safari suite
---
```

## Command: show privacy report

**Description:** Show Safari's Privacy Report

<a name="show_credit_card_settings"></a>
```yaml
---
type: command
name: show credit card settings
suite: Safari suite
---
```

## Command: show credit card settings

**Description:** Show Safari Credit Card Settings.

<a name="tab"></a>
```yaml
---
type: class
name: tab
suite: Safari suite
---
```

## Class: tab

**Description:** A Safari window tab.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| source | The HTML source of the web page currently loaded in the tab. | text | r |
| URL | The current URL of the tab. | text | read/write |
| index | The index of the tab, ordered left to right. | number | r |
| text | The text of the web page currently loaded in the tab. Modifications to text aren't reflected on the web page. | text | r |
| visible | Whether the tab is currently visible. | boolean | r |
| name | The name of the tab. | text | r |
| pid | The pid of the WebContent process backing the tab, if it exists. | number | r |

### Responds To
- **Command:** do JavaScript
- **Command:** email contents
- **Command:** close
- **Command:** search the web
<a name="sourceprovider"></a>
```yaml
---
type: class
name: sourceProvider
suite: Safari suite
---
```

## Class: sourceProvider

### Responds To
- **Command:** get
<a name="contentsprovider"></a>
```yaml
---
type: class
name: contentsProvider
suite: Safari suite
---
```

## Class: contentsProvider

### Responds To
- **Command:** get
<a name="window"></a>
```yaml
---
type: class-extension
name: window
suite: Safari suite
---
```

## Class Extension: window

**Description:** A Safari window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| current tab | The current tab. | tab | read/write |

### Elements
- **Type:** tab
<a name="document"></a>
```yaml
---
type: class-extension
name: document
suite: Safari suite
---
```

## Class Extension: document

**Description:** A Safari document representing the active tab in a window.

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| source | The HTML source of the web page currently loaded in the document. | text | r |
| URL | The current URL of the document. | text | read/write |
| text | The text of the web page currently loaded in the document. Modifications to text aren't reflected on the web page. | text | r |

### Responds To
- **Command:** do JavaScript
- **Command:** email contents
- **Command:** search the web
