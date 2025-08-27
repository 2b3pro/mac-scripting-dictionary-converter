# DEVONagent Suite: AppleScript/JSX Dictionary

## Table of Contents

### Commands
- [download markup from](#download_markup_from)
- [convert feed to HTML](#convert_feed_to_html)
- [get frames of](#get_frames_of)
- [hide progress indicator](#hide_progress_indicator)
- [get rich text of](#get_rich_text_of)
- [add download](#add_download)
- [archive](#archive)
- [stop downloads](#stop_downloads)
- [display name editor](#display_name_editor)
- [get cached data for URL](#get_cached_data_for_url)
- [download URL](#download_url)
- [open tab](#open_tab)
- [load workspace](#load_workspace)
- [append search](#append_search)
- [get links of](#get_links_of)
- [do JavaScript](#do_javascript)
- [get favicon of](#get_favicon_of)
- [search](#search)
- [get embedded images of](#get_embedded_images_of)
- [get embedded objects of](#get_embedded_objects_of)
- [step progress indicator](#step_progress_indicator)
- [start downloads](#start_downloads)
- [get title of](#get_title_of)
- [get scanner objects of](#get_scanner_objects_of)
- [get URL](#get_url)
- [add bookmark](#add_bookmark)
- [save workspace](#save_workspace)
- [open URL](#open_url)
- [delete](#delete)
- [show progress indicator](#show_progress_indicator)
- [get text of](#get_text_of)
- [delete workspace](#delete_workspace)
- [download JSON from](#download_json_from)
- [get items of feed](#get_items_of_feed)
- [get embedded sheets and scripts of](#get_embedded_sheets_and_scripts_of)
- [display authentication dialog](#display_authentication_dialog)
### Classes
- [application](#application)
- [search window](#search_window)
- [search result](#search_result)
- [browser](#browser)
- [tab](#tab)


## DEVONagent Suite

**Description:** DEVONagent's AppleScript Interface

### Commands
<a name="download_markup_from"></a>
```yaml
---

type: command
name: download markup from
suite: DEVONagent Suite
---
```

## Command: download markup from

**Description:** Download an HTML or XML page (including RSS, RDF or Atom feeds).

### Direct Parameter
- **Description:** The URL of the HTML or XML page to download.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| method | The HTTP method (\"GET\" by default) | text | Yes |
| password | The password for protected websites. | text | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary | Yes |
| referrer | The HTTP referrer. | text | Yes |
| agent | The user agent. | text | Yes |
| encoding | The encoding of the page (default ISO-Latin-1). | text | Yes |
| user | The user name for protected websites. | text | Yes |

### Result
- **Types:** text
<a name="convert_feed_to_html"></a>
```yaml
---

type: command
name: convert feed to HTML
suite: DEVONagent Suite
---
```

## Command: convert feed to HTML

**Description:** Convert a RSS, RDF or Atom feed to HTML.

### Direct Parameter
- **Description:** The source code of the feed.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the feed. | text | Yes |

### Result
- **Types:** text
<a name="get_frames_of"></a>
```yaml
---

type: command
name: get frames of
suite: DEVONagent Suite
---
```

## Command: get frames of

**Description:** Get the URLs of all frames of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the frames. | text | Yes |

### Result
- **Types:** list
<a name="hide_progress_indicator"></a>
```yaml
---

type: command
name: hide progress indicator
suite: DEVONagent Suite
---
```

## Command: hide progress indicator

**Description:** Hide a visible progress indicator.

### Result
- **Types:** boolean
<a name="get_rich_text_of"></a>
```yaml
---

type: command
name: get rich text of
suite: DEVONagent Suite
---
```

## Command: get rich text of

**Description:** Get the rich text of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page | text | Yes |

### Result
- **Types:** rich text
<a name="add_download"></a>
```yaml
---

type: command
name: add download
suite: DEVONagent Suite
---
```

## Command: add download

**Description:** Add a URL to the download manager.

### Direct Parameter
- **Description:** The URL to add.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| referrer | The HTTP referrer. | text | Yes |
| user | The user name for protected websites. | text | Yes |
| password | The password for protected websites. | text | Yes |

### Result
- **Types:** boolean
<a name="archive"></a>
```yaml
---

type: command
name: archive
suite: DEVONagent Suite
---
```

## Command: archive

**Description:** Add a search result to the archive.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| search result | The result to archive. | record item | No |

### Result
- **Types:** boolean
<a name="stop_downloads"></a>
```yaml
---

type: command
name: stop downloads
suite: DEVONagent Suite
---
```

## Command: stop downloads

**Description:** Stop queue of download manager.

### Result
- **Types:** boolean
<a name="display_name_editor"></a>
```yaml
---

type: command
name: display name editor
suite: DEVONagent Suite
---
```

## Command: display name editor

**Description:** Display a dialog to enter a name.

### Direct Parameter
- **Description:** The title of the dialog. By default the application name.
- **Types:** text
- **Optional:** Yes
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| info | The info for the dialog. | text | Yes |
| default answer | The default editable name. | text | Yes |

### Result
- **Types:** text
<a name="get_cached_data_for_url"></a>
```yaml
---

type: command
name: get cached data for URL
suite: DEVONagent Suite
---
```

## Command: get cached data for URL

**Description:** Get cached data for URL of a resource which is part of a loaded webpage and its DOM tree, rendered in a browser tab/window.

### Direct Parameter
- **Description:** The URL.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| from | The source browser tab. Uses current tab of frontmost browser window otherwise. | browser tab | Yes |

### Result
- **Types:** raw data
<a name="download_url"></a>
```yaml
---

type: command
name: download URL
suite: DEVONagent Suite
---
```

## Command: download URL

**Description:** Download a URL.

### Direct Parameter
- **Description:** The URL to download.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| password | The password for protected websites. | text | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary | Yes |
| method | The HTTP method (\"GET\" by default) | text | Yes |
| referrer | The HTTP referrer. | text | Yes |
| agent | The user agent. | text | Yes |
| user | The user name for protected websites. | text | Yes |

### Result
- **Types:** raw data
<a name="open_tab"></a>
```yaml
---

type: command
name: open tab
suite: DEVONagent Suite
---
```

## Command: open tab

**Description:** Opens an optional URL in a new tab in the specified browser window or in a new browser window if none is specified.

### Direct Parameter
- **Description:** The optional URL to open.
- **Types:** text
- **Optional:** Yes
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| referrer | The HTTP referrer. | text | Yes |
| in | The optional browser window that should open a new tab. | browser window | Yes |

### Result
- **Types:** brtb
<a name="load_workspace"></a>
```yaml
---

type: command
name: load workspace
suite: DEVONagent Suite
---
```

## Command: load workspace

**Description:** Load a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
- **Optional:** No
### Result
- **Types:** boolean
<a name="append_search"></a>
```yaml
---

type: command
name: append search
suite: DEVONagent Suite
---
```

## Command: append search

**Description:** Append a search to a search window using either a search set or a plugin.

### Direct Parameter
- **Description:** The query. Optional for search sets having a default query.
- **Types:** text
- **Optional:** Yes
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using set | The name of the search set to use. | text | Yes |
| to | The search window. | query window | No |
| using plugin | The identifier of the plugin to use. | text | Yes |

### Result
- **Types:** boolean
<a name="get_links_of"></a>
```yaml
---

type: command
name: get links of
suite: DEVONagent Suite
---
```

## Command: get links of

**Description:** Get the URLs of all links of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the links. | text | Yes |
| containing | The case sensitive string matched against the description of links. | text | Yes |
| type | The desired type of the links (e.g. HTML, PHP, JPG, ...). | text | Yes |

### Result
- **Types:** list
<a name="do_javascript"></a>
```yaml
---

type: command
name: do JavaScript
suite: DEVONagent Suite
---
```

## Command: do JavaScript

**Description:** Applies a string of JavaScript code to a browser.

### Direct Parameter
- **Description:** The code.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| in | The browser window/tab that the JavaScript should be applied in. | browser window | No |

### Result
- **Types:** text
<a name="get_favicon_of"></a>
```yaml
---

type: command
name: get favicon of
suite: DEVONagent Suite
---
```

## Command: get favicon of

**Description:** Get the favicon of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the favicon. | text | Yes |

### Result
- **Types:** text
<a name="search"></a>
```yaml
---

type: command
name: search
suite: DEVONagent Suite
---
```

## Command: search

**Description:** Start a search using either a search set or a plugin.

### Direct Parameter
- **Description:** The query. Optional for search sets having a default query.
- **Types:** text
- **Optional:** Yes
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| using set | The name of the search set to use. | text | Yes |
| minimized window | Open a minimized search window. | boolean | Yes |
| using plugin | The identifier of the plugin to use. | text | Yes |

### Result
- **Types:** boolean
<a name="get_embedded_images_of"></a>
```yaml
---

type: command
name: get embedded images of
suite: DEVONagent Suite
---
```

## Command: get embedded images of

**Description:** Get the URLs of all embedded images of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the images. | text | Yes |
| type | The desired type of the images (e.g. JPG, GIF, PNG, ...). | text | Yes |

### Result
- **Types:** list
<a name="get_embedded_objects_of"></a>
```yaml
---

type: command
name: get embedded objects of
suite: DEVONagent Suite
---
```

## Command: get embedded objects of

**Description:** Get the URLs of all embedded objects of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the embedded objects | text | Yes |
| type | The desired type of the objects (e.g. MOV). | text | Yes |

### Result
- **Types:** list
<a name="step_progress_indicator"></a>
```yaml
---

type: command
name: step progress indicator
suite: DEVONagent Suite
---
```

## Command: step progress indicator

**Description:** Go to next step of a progress.

### Direct Parameter
- **Description:** The info for the current step.
- **Types:** text
- **Optional:** Yes
### Result
- **Types:** boolean
<a name="start_downloads"></a>
```yaml
---

type: command
name: start downloads
suite: DEVONagent Suite
---
```

## Command: start downloads

**Description:** Start queue of download manager.

### Result
- **Types:** boolean
<a name="get_title_of"></a>
```yaml
---

type: command
name: get title of
suite: DEVONagent Suite
---
```

## Command: get title of

**Description:** Get the title of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Result
- **Types:** text
<a name="get_scanner_objects_of"></a>
```yaml
---

type: command
name: get scanner objects of
suite: DEVONagent Suite
---
```

## Command: get scanner objects of

**Description:** Get the scanner objects of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page. | text | No |
| scanner | The identifier of the scanner. | text | No |

### Result
- **Types:** list
<a name="get_url"></a>
```yaml
---

type: command
name: get URL
suite: DEVONagent Suite
---
```

## Command: get URL

**Description:** Open a URL. Use \"open URL\" in scripts, this command is for external applications and might open a new window or use the current one depending on the preferences.

<a name="add_bookmark"></a>
```yaml
---

type: command
name: add bookmark
suite: DEVONagent Suite
---
```

## Command: add bookmark

**Description:** Add a URL to the bookmarks.

### Direct Parameter
- **Description:** The URL to add.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| name | The name of the bookmark. | text | Yes |

### Result
- **Types:** boolean
<a name="save_workspace"></a>
```yaml
---

type: command
name: save workspace
suite: DEVONagent Suite
---
```

## Command: save workspace

**Description:** Save a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
- **Optional:** No
### Result
- **Types:** boolean
<a name="open_url"></a>
```yaml
---

type: command
name: open URL
suite: DEVONagent Suite
---
```

## Command: open URL

**Description:** Open a URL

### Direct Parameter
- **Description:** The URL to open.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| referrer | The HTTP referrer. | text | Yes |

<a name="delete"></a>
```yaml
---

type: command
name: delete
suite: DEVONagent Suite
---
```

## Command: delete

**Description:** Delete a search result.

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| search result | The result to delete. | record item | No |

### Result
- **Types:** boolean
<a name="show_progress_indicator"></a>
```yaml
---

type: command
name: show progress indicator
suite: DEVONagent Suite
---
```

## Command: show progress indicator

**Description:** Show a progress indicator or update an already visible indicator. You have to ensure that the indicator is hidden again via 'hide progress indicator' when the script ends or if an error occurs.

### Direct Parameter
- **Description:** The title of the progress.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| steps | The number of steps of the progress or a negative value for an indeterminate number. | number | Yes |
| cancel button | Display a button to cancel the process. | boolean | Yes |

### Result
- **Types:** boolean
<a name="get_text_of"></a>
```yaml
---

type: command
name: get text of
suite: DEVONagent Suite
---
```

## Command: get text of

**Description:** Get the plain text of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Result
- **Types:** text
<a name="delete_workspace"></a>
```yaml
---

type: command
name: delete workspace
suite: DEVONagent Suite
---
```

## Command: delete workspace

**Description:** Delete a workspace.

### Direct Parameter
- **Description:** The name of the workspace.
- **Types:** text
- **Optional:** No
### Result
- **Types:** boolean
<a name="download_json_from"></a>
```yaml
---

type: command
name: download JSON from
suite: DEVONagent Suite
---
```

## Command: download JSON from

**Description:** Download a JSON object.

### Direct Parameter
- **Description:** The URL of the JSON object.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| password | The password for protected websites. | text | Yes |
| post | A dictionary containing key-value pairs for HTTP POST actions. | dictionary | Yes |
| method | The HTTP method (\"GET\" by default) | text | Yes |
| referrer | The HTTP referrer. | text | Yes |
| agent | The user agent. | text | Yes |
| user | The user name for protected websites. | text | Yes |

### Result
- **Types:** record
<a name="get_items_of_feed"></a>
```yaml
---

type: command
name: get items of feed
suite: DEVONagent Suite
---
```

## Command: get items of feed

**Description:** Get the items of a RSS, RDF or Atom feed. Dictionaries contain title (text), link (text), date (text), description (text), content (text), author (text), html (item converted to HTML), tags (list) and enclosures (list)

### Direct Parameter
- **Description:** The source code of the feed.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the feed. | text | Yes |

### Result
- **Types:** list
<a name="get_embedded_sheets_and_scripts_of"></a>
```yaml
---

type: command
name: get embedded sheets and scripts of
suite: DEVONagent Suite
---
```

## Command: get embedded sheets and scripts of

**Description:** Get the URLs of all embedded style sheets and scripts of an HTML page.

### Direct Parameter
- **Description:** The source code of the HTML page.
- **Types:** text
- **Optional:** No
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| base URL | The URL of the HTML page containing the style sheets and scripts. | text | Yes |
| type | The desired type of the links (e.g. CSS). | text | Yes |

### Result
- **Types:** list
<a name="display_authentication_dialog"></a>
```yaml
---

type: command
name: display authentication dialog
suite: DEVONagent Suite
---
```

## Command: display authentication dialog

**Description:** Display a dialog to enter a username and its password.

### Direct Parameter
- **Description:** The info for the dialog.
- **Types:** text
- **Optional:** Yes
### Result
- **Types:** record
### Classes
<a name="application"></a>
```yaml
type: class
---

name: application
suite: DEVONagent Suite
---
```

## Class: application

**Description:** DEVONagent's top level scripting object.

**Inherits:** NSCoreSuite.NSApplication

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| search sets | The names of all available search sets. | list | read only |
| plugins | The identifiers of all enabled plugins. | list | read only |
| cancelled progress | Specifies if a process with a visible progress indicator should be cancelled. | boolean | read only |
| last downloaded URL | The actual URL of the last download. | text | read only |
| last downloaded response | HTTP-Status, Last-Modified, Content-Type, Content-Length and Charset of last HTTP(S) response. | dictionary | read only |
| workspaces | The names of all available workspaces. | list | read only |

### Elements
- **Type:** browser window
- **Type:** query window
<a name="search_window"></a>
```yaml
type: class
---

name: search window
suite: DEVONagent Suite
---
```

## Class: search window

**Description:** A DEVONagent search window (supports standard 'print' and 'close' commands).

**Inherits:** NSCoreSuite.NSWindow

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| selection | The selected results. | list | read only |
| searching | Specifies if the window is still searching. | boolean | read only |

### Elements
- **Type:** record item
### Responds To
- **Command:** Close"
- **Command:** Print"
<a name="search_result"></a>
```yaml
type: class
---

name: search result
suite: DEVONagent Suite
---
```

## Class: search result

**Description:** A DEVONagent search result.

**Inherits:** NSCoreSuite.AbstractObject

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| source | The HTML source of the result. | text | read only |
| summary | Abstract of the result. | text | read only |
| score | Score of the result. | real | read only |
| title | Title of the result. | text | read only |
| URL | The URL of the result. | text | read only |
| text | Text of the result. | text | read only |
| date | Date of the result. | date | read only |
| scanner objects | The objects of the result found by the used scanner. | list | read only |
| id | The scripting identifier of a search result. | integer | read only |

<a name="browser"></a>
```yaml
type: class
---

name: browser
suite: DEVONagent Suite
---
```

## Class: browser

**Description:** A DEVONagent browser window (supports standard 'save', 'print' and 'close' commands).

**Inherits:** NSCoreSuite.NSWindow

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| source | The HTML source of the current web page. | text | read only |
| paginated PDF | A printed PDF with pagination of the current web page. | raw data | read only |
| web archive | Web archive of the current web page. | raw data | read only |
| loading | Specifies if the current web page is still loading. | boolean | read only |
| URL | The URL of the current web page. | text | read/write |
| current result | The currently displayed search result. | record item | read only |
| text | Text of the current web page. A copy. Modifications to text aren't reflected on the web page. | rich text | read only |
| PDF | A PDF without pagination of the current web page retaining the screen layout. | raw data | read only |
| scanner objects | The objects for the currently selected scanner or for the scanner used for searching. | list | read only |
| current tab | The selected tab of the browser window. | browser tab | read/write |

### Elements
- **Type:** browser tab
### Responds To
- **Command:** Print"
- **Command:** Save"
- **Command:** Close"
<a name="tab"></a>
```yaml
type: class
---

name: tab
suite: DEVONagent Suite
---
```

## Class: tab

**Description:** A tab of a browser window (supports standard 'save', 'print' and 'close' commands).

**Inherits:** NSCoreSuite.AbstractObject

### Properties
| Name | Description | Type | Access |
|---|---|---|---|
| paginated PDF | A printed PDF with pagination of the current web page. | raw data | read only |
| current result | The currently displayed search result. | record item | read only |
| loading | Specifies if the current web page is still loading. | boolean | read only |
| scanner objects | The objects for the currently selected scanner or for the scanner used for searching. | list | read only |
| web archive | Web archive of the current web page. | raw data | read only |
| id | The unique identifier of the tab. | integer | read only |
| URL | The URL of the current web page. | text | read/write |
| source | The HTML source of the current web page. | text | read only |
| name | The full title of the tab. | text | read only |
| text | Text of the current web page. A copy. Modifications to text aren't reflected on the web page. | rich text | read only |
| PDF | A PDF without pagination of the current web page retaining the screen layout. | raw data | read only |
| browser | The browser window of the tab. | browser window | read only |

### Responds To
- **Command:** Print"
- **Command:** Save"
- **Command:** Close"
