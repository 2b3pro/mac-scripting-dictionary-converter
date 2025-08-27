# Better Touch Tool (BTT) Terminology: AppleScript/JSX

## Table of Contents

### BetterTouchTool Script Suite
#### Commands
- [get_location](#get_location)
- [chat_gpt](#chat_gpt)
- [get_dock_badge_for](#get_dock_badge_for)
- [get_menubar_menuitem_details](#get_menubar_menuitem_details)
- [get_menu_item_details](#get_menu_item_details)
- [is_app_running](#is_app_running)
- [set_persistent_string_variable](#set_persistent_string_variable)
- [set_string_variable](#set_string_variable)
- [set_persistent_number_variable](#set_persistent_number_variable)
- [set_number_variable](#set_number_variable)
- [get_active_touch_bar_group](#get_active_touch_bar_group)
- [get_string_variable](#get_string_variable)
- [reveal_element_in_ui](#reveal_element_in_ui)
- [get_weather](#get_weather)
- [get_menu_item_value](#get_menu_item_value)
- [update_menu_item](#update_menu_item)
- [set_menu_item_value](#set_menu_item_value)
- [webview_menu_item_load_html_url_js](#webview_menu_item_load_html_url_js)
- [get_number_variable](#get_number_variable)
- [is_true_tone_enabled](#is_true_tone_enabled)
- [trigger_named_async_without_response](#trigger_named_async_without_response)
- [cancel_delayed_named_trigger_execution](#cancel_delayed_named_trigger_execution)
- [trigger_named](#trigger_named)
- [run_shortcut](#run_shortcut)
- [trigger_action](#trigger_action)
- [get_trigger](#get_trigger)
- [get_preset_details](#get_preset_details)
- [delete_triggers](#delete_triggers)
- [get_triggers](#get_triggers)
- [delete_trigger](#delete_trigger)
- [execute_assigned_actions_for_trigger](#execute_assigned_actions_for_trigger)
- [add_new_trigger](#add_new_trigger)
- [update_trigger](#update_trigger)
- [refresh_widget](#refresh_widget)
- [update_touch_bar_widget](#update_touch_bar_widget)
- [update_stream_deck_widget](#update_stream_deck_widget)
- [display_notification](#display_notification)
- [set_clipboard_content](#set_clipboard_content)
- [set_clipboard_content](#set_clipboard_content)
- [get_selection](#get_selection)
- [get_clipboard_content](#get_clipboard_content)
- [paste_text](#paste_text)
- [update_menubar_item](#update_menubar_item)
- [import_preset](#import_preset)
- [export_preset](#export_preset)
#### Classs
- [application](#application)


## BetterTouchTool Script Suite

**Description:** BetterTouchTool Script Suite.

<a name="get_location"></a>
```yaml
---
type: command
name: get_location
suite: BetterTouchTool Script Suite
---
```

## Command: get_location

**Description:** This returns the approximate location of your Mac.

### Direct Parameter
- **Description:** This returns the approximate location of your Mac.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The value of the variable
- **Types:** text
<a name="chat_gpt"></a>
```yaml
---
type: command
name: chat_gpt
suite: BetterTouchTool Script Suite
---
```

## Command: chat_gpt

**Description:** Call ChatGPT

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| identifier | An identifier to keep history | text | Yes |
| user | The user request (what you ask chatgpt to do) | text | Yes |
| system | Tell ChatGPT how it should behave | text | Yes |
| input | Additional input for your request | text | Yes |
| maxHistory | Max number of history items to include | number | Yes |
| stream | Stream reply | boolean | Yes |
| customURL | Custom URL (to use API compatible services) | text | Yes |
| apiKey | API Key (will be saved, so you don't need to pass it every time) | text | Yes |
| model | The model to use (default is gpt-4o-mini), others only work if you provide an API key | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The badge label
- **Types:** text
<a name="get_dock_badge_for"></a>
```yaml
---
type: command
name: get_dock_badge_for
suite: BetterTouchTool Script Suite
---
```

## Command: get_dock_badge_for

**Description:** This retrieves the dock badge for the given application name.

### Direct Parameter
- **Description:** The name of the app
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| update_interval | This defines how often the data that is returned by this function is updated inside BTT. If set to a negative value, it will not update anymore. Default is -1. | number | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The badge label
- **Types:** text
<a name="get_menubar_menuitem_details"></a>
```yaml
---
type: command
name: get_menubar_menuitem_details
suite: BetterTouchTool Script Suite
---
```

## Command: get_menubar_menuitem_details

**Description:** This gets the status for a specific menu item. E.g. Edit;Format;Font;Bold

### Direct Parameter
- **Description:** The path to the menu item. E.g. Edit;Format;Font;Bold
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| item_path | The path to the item | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Some JSON with the result
- **Types:** text
<a name="get_menu_item_details"></a>
```yaml
---
type: command
name: get_menu_item_details
suite: BetterTouchTool Script Suite
---
```

## Command: get_menu_item_details

**Description:** This gets the status for a specific menu item. E.g. Edit;Format;Font;Bold

### Direct Parameter
- **Description:** The path to the menu item. E.g. Edit;Format;Font;Bold
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| item_path | The path to the item | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Some JSON with the result
- **Types:** text
<a name="is_app_running"></a>
```yaml
---
type: command
name: is_app_running
suite: BetterTouchTool Script Suite
---
```

## Command: is_app_running

**Description:** This allows you to find out whether the given app is currently running

### Direct Parameter
- **Description:** The name or bundle identifier of the app
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The result
- **Types:** boolean
<a name="set_persistent_string_variable"></a>
```yaml
---
type: command
name: set_persistent_string_variable
suite: BetterTouchTool Script Suite
---
```

## Command: set_persistent_string_variable

**Description:** This allows you to set a variable to a given string that persists over BTT relaunches.

### Direct Parameter
- **Description:** The name of the persistent variable you want to set
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The value of the persistent variable | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="set_string_variable"></a>
```yaml
---
type: command
name: set_string_variable
suite: BetterTouchTool Script Suite
---
```

## Command: set_string_variable

**Description:** This allows you to set a variable to a given string for the runtime of BTT.

### Direct Parameter
- **Description:** The name of the variable you want to set
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The value of the variable | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="set_persistent_number_variable"></a>
```yaml
---
type: command
name: set_persistent_number_variable
suite: BetterTouchTool Script Suite
---
```

## Command: set_persistent_number_variable

**Description:** This allows you to set a variable to a given number that persists over BTT relaunches.

### Direct Parameter
- **Description:** The name of the persistent variable you want to set
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The value of the persistent variable | number | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="set_number_variable"></a>
```yaml
---
type: command
name: set_number_variable
suite: BetterTouchTool Script Suite
---
```

## Command: set_number_variable

**Description:** This allows you to set a variable to a given number for the runtime of BTT.

### Direct Parameter
- **Description:** The name of the variable you want to set
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| to | The value of the variable | real | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="get_active_touch_bar_group"></a>
```yaml
---
type: command
name: get_active_touch_bar_group
suite: BetterTouchTool Script Suite
---
```

## Command: get_active_touch_bar_group

**Description:** This allows you to get the currently active Touch Bar Group.

### Result
- **Description:** The value of the group
- **Types:** text
<a name="get_string_variable"></a>
```yaml
---
type: command
name: get_string_variable
suite: BetterTouchTool Script Suite
---
```

## Command: get_string_variable

**Description:** This allows you to get the value of a previously set string variable in BTT.

### Direct Parameter
- **Description:** The name of the variable you want to get
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |
| default | The default value of the variable | text | Yes |

### Result
- **Description:** The value of the variable
- **Types:** text
<a name="reveal_element_in_ui"></a>
```yaml
---
type: command
name: reveal_element_in_ui
suite: BetterTouchTool Script Suite
---
```

## Command: reveal_element_in_ui

**Description:** This allows you to show a specific element in the BTT UI

### Direct Parameter
- **Description:** The UUID of the item you want to access
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Result
- **Types:** text
<a name="get_weather"></a>
```yaml
---
type: command
name: get_weather
suite: BetterTouchTool Script Suite
---
```

## Command: get_weather

**Description:** This allows you to get the current weather for a location. Powered by Apple Weather / WeatherKit.

### Direct Parameter
- **Description:** The location in this format {LAT},{LON}
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| unit | The unit (celsius or fahrenheit) | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** A JSON string
- **Types:** text
<a name="get_menu_item_value"></a>
```yaml
---
type: command
name: get_menu_item_value
suite: BetterTouchTool Script Suite
---
```

## Command: get_menu_item_value

**Description:** This allows you to get the current value of an item in a floating menu.

### Direct Parameter
- **Description:** The UUID of the item you want to access (alternatively you can specify the menu name and item name)
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| menu_name | The name of the menu that contains the item | text | Yes |
| item_name | The name of the item | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The current value of the item
- **Types:** any
<a name="update_menu_item"></a>
```yaml
---
type: command
name: update_menu_item
suite: BetterTouchTool Script Suite
---
```

## Command: update_menu_item

**Description:** Update any property of a menu item.

### Direct Parameter
- **Description:** The UUID of the item you want to access (alternatively you can specify the menu name and item name)
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| menu_name | The name of the menu that contains the item | text | Yes |
| item_name | The name of the item | text | Yes |
| json | The json (as string) containing the properties to update | text | No |
| persist | Persist the change | boolean | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Done
- **Types:** text
<a name="set_menu_item_value"></a>
```yaml
---
type: command
name: set_menu_item_value
suite: BetterTouchTool Script Suite
---
```

## Command: set_menu_item_value

**Description:** This allows you to set the current value of an item in a floating menu.

### Direct Parameter
- **Description:** The UUID of the item you want to access (alternatively you can specify the menu name and item name)
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| menu_name | The name of the menu that contains the item | text | Yes |
| item_name | The name of the item | text | Yes |
| value | The value to assign to the item | any | No |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The current value of the item
- **Types:** text
<a name="webview_menu_item_load_html_url_js"></a>
```yaml
---
type: command
name: webview_menu_item_load_html_url_js
suite: BetterTouchTool Script Suite
---
```

## Command: webview_menu_item_load_html_url_js

**Description:** This allows to load HTML or a URL into the specified webview menu item. It can also execute arbitrary JavaScript on the item's content

### Direct Parameter
- **Description:** The UUID of the item you want to access (alternatively you can specify the menu name and item name)
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| menu_name | The name of the menu that contains the item | text | Yes |
| item_name | The name of the item | text | Yes |
| html_or_url | The HTML or URL to load into the webview item. URLs can start with http:, https: or file:. You can leave this empty and use the javascript_to_execute instead if you just want to execute some JS on the currently loaded content. | text | Yes |
| javascript_to_execute | The provided Java Script will be executed after loading the HTML or URL. If no HTML or URL is specified it will immediately be executed on the currently loaded content. | text | Yes |
| useragent | User Agent to use | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Status
- **Types:** text
<a name="get_number_variable"></a>
```yaml
---
type: command
name: get_number_variable
suite: BetterTouchTool Script Suite
---
```

## Command: get_number_variable

**Description:** This allows you to get the value of a previously set string variable in BTT.

### Direct Parameter
- **Description:** The name of the variable you want to get
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| default | The default value of the variable | real | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The value of the variable
- **Types:** real
<a name="is_true_tone_enabled"></a>
```yaml
---
type: command
name: is_true_tone_enabled
suite: BetterTouchTool Script Suite
---
```

## Command: is_true_tone_enabled

**Description:** This returns true when true tone is currently enabled, false otherwise..

### Result
- **Description:** true when true tone is currently enabled, false otherwise
- **Types:** boolean
<a name="trigger_named_async_without_response"></a>
```yaml
---
type: command
name: trigger_named_async_without_response
suite: BetterTouchTool Script Suite
---
```

## Command: trigger_named_async_without_response

**Description:** This triggers one of the named triggers configured in the Other tab in BTT. It runs async and doesn't return a response.

### Direct Parameter
- **Description:** The name of the trigger.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| delay | The delay in seconds | real | Yes |
| cancel_delayed | Cancel any other delayed named triggers for the given name | boolean | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result is just a static value here
- **Types:** text
<a name="cancel_delayed_named_trigger_execution"></a>
```yaml
---
type: command
name: cancel_delayed_named_trigger_execution
suite: BetterTouchTool Script Suite
---
```

## Command: cancel_delayed_named_trigger_execution

**Description:** Cancels a delayed named trigger execution.

### Direct Parameter
- **Description:** The name of the trigger.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result is just a static value here
- **Types:** text
<a name="trigger_named"></a>
```yaml
---
type: command
name: trigger_named
suite: BetterTouchTool Script Suite
---
```

## Command: trigger_named

**Description:** This triggers one of the named triggers configured in the Other tab in BTT.

### Direct Parameter
- **Description:** The name of the trigger.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| cancel_delayed | Cancel any other delayed named triggers for the given name | boolean | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="run_shortcut"></a>
```yaml
---
type: command
name: run_shortcut
suite: BetterTouchTool Script Suite
---
```

## Command: run_shortcut

**Description:** This triggers a shortcut from the Shortcuts app.

### Direct Parameter
- **Description:** The name of the Shortcut.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="trigger_action"></a>
```yaml
---
type: command
name: trigger_action
suite: BetterTouchTool Script Suite
---
```

## Command: trigger_action

**Description:** This triggers a BTT predefined action without adding it to BTT

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, touch bar item etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool. Example usage: tell application BetterTouchTool trigger uuid theUUID end tell
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="get_trigger"></a>
```yaml
---
type: command
name: get_trigger
suite: BetterTouchTool Script Suite
---
```

## Command: get_trigger

**Description:** This returns the properties of the requested trigger

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, touch bar item etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool. Example usage: tell application BetterTouchTool trigger uuid theUUID end tell
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Trigger description
- **Types:** text
<a name="get_preset_details"></a>
```yaml
---
type: command
name: get_preset_details
suite: BetterTouchTool Script Suite
---
```

## Command: get_preset_details

**Description:** This returns the properties of the requested preset

### Direct Parameter
- **Description:** The uuid or name of the preset.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Preset description
- **Types:** text
<a name="delete_triggers"></a>
```yaml
---
type: command
name: delete_triggers
suite: BetterTouchTool Script Suite
---
```

## Command: delete_triggers

**Description:** This deletes all triggers matching the provided values (test with the get_triggers function first)

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| trigger_type | The type of the trigger, e.g. BTTTriggerTypeMagicMouse | text | Yes |
| trigger_id | The id of the trigger, e.g. 123 | number | Yes |
| trigger_uuid | The uuid of the trigger | text | Yes |
| trigger_app_bundle_identifier | The bundle identifier of the app you want to retrieve triggers for | text | Yes |
| preset | The preset you want to retrieve triggers for | text | Yes |
| trigger_parent_uuid | The UUID of the parent group / trigger | text | Yes |
| return_only_if_modifiers_match | If set only triggers that match the pressed modifier keys will be returned. | number | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Trigger description
- **Types:** text
<a name="get_triggers"></a>
```yaml
---
type: command
name: get_triggers
suite: BetterTouchTool Script Suite
---
```

## Command: get_triggers

**Description:** This returns all triggers matching the provided values

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| trigger_type | The type of the trigger, e.g. BTTTriggerTypeMagicMouse | text | Yes |
| trigger_id | The id of the trigger, e.g. 123 | number | Yes |
| trigger_uuid | The uuid of the trigger | text | Yes |
| trigger_app_bundle_identifier | The bundle identifier of the app you want to retrieve triggers for | text | Yes |
| trigger_parent_uuid | The UUID of the parent group / trigger | text | Yes |
| return_only_if_modifiers_match | If set only triggers that match the pressed modifier keys will be returned. | number | Yes |
| preset | The preset you want to retrieve triggers for | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Trigger description
- **Types:** text
<a name="delete_trigger"></a>
```yaml
---
type: command
name: delete_trigger
suite: BetterTouchTool Script Suite
---
```

## Command: delete_trigger

**Description:** This will delete the trigger (Gesture, Shortcut, etc.) with the given UUID

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool. Example usage: tell application BetterTouchTool trigger uuid theUUID end tell
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="execute_assigned_actions_for_trigger"></a>
```yaml
---
type: command
name: execute_assigned_actions_for_trigger
suite: BetterTouchTool Script Suite
---
```

## Command: execute_assigned_actions_for_trigger

**Description:** Make any configured trigger execute its assigned actions

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool. Example usage: tell application BetterTouchTool trigger uuid theUUID end tell
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="add_new_trigger"></a>
```yaml
---
type: command
name: add_new_trigger
suite: BetterTouchTool Script Suite
---
```

## Command: add_new_trigger

**Description:** Add a new BetterTouchTool trigger via JSON input

### Direct Parameter
- **Description:** This must be a JSON dictionary string which can contain all keys and properties that are allowed in BTT's JSON export. You can get them for a specific gesture/trigger by right-clicking it and choosing 'Copy JSON'
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| parent_uuid | If you want to add the trigger to a group, specify the group uuid as parent here. | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The uuid of the created trigger
- **Types:** text
<a name="update_trigger"></a>
```yaml
---
type: command
name: update_trigger
suite: BetterTouchTool Script Suite
---
```

## Command: update_trigger

**Description:** Update the properties of any BetterTouchTool trigger. 

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| json | This must be a JSON dictionary string which can contain all keys and properties that are allowed in BTT's JSON export. You can get them for a specific gesture/trigger by right-clicking it and choosing 'Copy JSON' | text | No |
| trigger_parent_uuid | The UUID of the parent group / trigger | text | Yes |
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** The uuid of the created or updated trigger
- **Types:** text
<a name="refresh_widget"></a>
```yaml
---
type: command
name: refresh_widget
suite: BetterTouchTool Script Suite
---
```

## Command: refresh_widget

**Description:** Run a Touch Bar widget's assigned script to update the widget.

### Direct Parameter
- **Description:** The uuid of the trigger (gesture, shortcut, etc.). You can get it by right-clicking a trigger you set up in BetterTouchTool.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

<a name="update_touch_bar_widget"></a>
```yaml
---
type: command
name: update_touch_bar_widget
suite: BetterTouchTool Script Suite
---
```

## Command: update_touch_bar_widget

**Description:** Provide new content to a Touch Bar script widget without triggering the script

### Direct Parameter
- **Description:** The uuid of Touch Bar widget you want to update. You can get it by right-clicking the widget you set up in BetterTouchTool.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |
| text | The text you want to show in the widget | text | Yes |
| icon_path | A file path to an icon that should be loaded | text | Yes |
| sf_symbol_name | The name of the sf symbol to load | text | Yes |
| sf_symbol_size | The size of the sf symbol to load | number | Yes |
| sf_symbol_weight | The weight of the sf symbol to load | number | Yes |
| icon_data | The base64 encoded icon data of the icon you want to show on the Touch Bar widget | text | Yes |
| background_color | The background color the widget should have. Must be in this format (RGBA): 255,255,255,255 | text | Yes |

<a name="update_stream_deck_widget"></a>
```yaml
---
type: command
name: update_stream_deck_widget
suite: BetterTouchTool Script Suite
---
```

## Command: update_stream_deck_widget

**Description:** Provide new content to a Stream Deck script widget without triggering the script

### Direct Parameter
- **Description:** The uuid of Stream Deck widget you want to update. You can get it by right-clicking the widget you set up in BetterTouchTool.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |
| text | The text you want to show in the widget | text | Yes |
| json | A JSON string containing all the properties you want to update | text | Yes |

<a name="display_notification"></a>
```yaml
---
type: command
name: display_notification
suite: BetterTouchTool Script Suite
---
```

## Command: display_notification

**Description:** Display a notification in Notification Center

### Direct Parameter
- **Description:** Notification body
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| with title | Title | text | Yes |
| subtitle | The subtitle | text | Yes |
| sound name | Sound name | text | Yes |
| image path | Image path | text | Yes |

<a name="set_clipboard_content"></a>
```yaml
---
type: command
name: set_clipboard_content
suite: BetterTouchTool Script Suite
---
```

## Command: set_clipboard_content

**Description:** Set the current clipboard content

### Direct Parameter
- **Description:** Text to set
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| content | Text / content to set | text | Yes |
| format | Clipboard Content Format | text | Yes |

<a name="set_clipboard_content"></a>
```yaml
---
type: command
name: set_clipboard_content
suite: BetterTouchTool Script Suite
---
```

## Command: set_clipboard_content

**Description:** Set the current clipboard content

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| contents | List of text contents to set | list of text | No |
| formats | List of formats | list of text | Yes |

<a name="get_selection"></a>
```yaml
---
type: command
name: get_selection
suite: BetterTouchTool Script Suite
---
```

## Command: get_selection

**Description:** Get the current selected text / item

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| format | Data Type / Format to get | text | Yes |
| asBase64 | Return as Base64 | boolean | Yes |

### Result
- **Description:** The selection
- **Types:** text
<a name="get_clipboard_content"></a>
```yaml
---
type: command
name: get_clipboard_content
suite: BetterTouchTool Script Suite
---
```

## Command: get_clipboard_content

**Description:** Get the current clipboard content

### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| format | Data Type / Format to get | text | Yes |
| asBase64 | Return as Base64 | boolean | Yes |

### Result
- **Description:** The content of the clipboard
- **Types:** text
<a name="paste_text"></a>
```yaml
---
type: command
name: paste_text
suite: BetterTouchTool Script Suite
---
```

## Command: paste_text

**Description:** Paste a string

### Direct Parameter
- **Description:** String To Paste
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| text | Text to Paste | text | Yes |
| format | Paste Format | text | Yes |
| insert_by_pasting | Insert By Pasting | boolean | Yes |
| move_cursor_left_by_x_after_pasting | Move Text Cursor Left by X After Pasting | number | Yes |

<a name="update_menubar_item"></a>
```yaml
---
type: command
name: update_menubar_item
suite: BetterTouchTool Script Suite
---
```

## Command: update_menubar_item

**Description:** Provide new content to a scriptable BTT Menu Bar Item without triggering the assigned script

### Direct Parameter
- **Description:** The uuid of Menu Bar Item you want to update. You can get it by right-clicking the item you set up in BetterTouchTool.
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |
| text | The text you want to show in the menubar item | text | Yes |
| hidden | Define whether the item should be hidden | boolean | Yes |
| icon_path | A file path to an icon that should be loaded | text | Yes |
| icon_data | The base64 encoded icon data of the icon you want to show on the menubar item | text | Yes |
| sf_symbol_name | The name of the sf symbol to load | text | Yes |
| sf_symbol_size | The size of the sf symbol to load | number | Yes |
| sf_symbol_weight | The weight of the sf symbol to load | number | Yes |
| background_color | The background color the menubar item should have. Must be in this format (RGBA): 255,255,255,255 | text | Yes |
| font_color | The font and sfsymbol color the menubar item should have. Must be in this format (RGBA): 255,255,255,255 | text | Yes |

<a name="import_preset"></a>
```yaml
---
type: command
name: import_preset
suite: BetterTouchTool Script Suite
---
```

## Command: import_preset

**Description:** Import a preset by file path

### Direct Parameter
- **Description:** The file path leading to the preset
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="export_preset"></a>
```yaml
---
type: command
name: export_preset
suite: BetterTouchTool Script Suite
---
```

## Command: export_preset

**Description:** Exports a preset by name

### Direct Parameter
- **Description:** The name of the preset
- **Types:** text
### Parameters
| Name | Description | Type | Optional |
|---|---|---|---|
| shared_secret | You can specify a shared secret which must be contained in all Apple Script calls in the advanced BTT preferences. | text | Yes |
| comment | Some comment | text | Yes |
| outputPath | The output path | text | No |
| link | If you want to show a link while importing the preset provide this. | text | Yes |
| compress | Compress the preset | boolean | Yes |
| includeSettings | Whether to include exportable general settings | boolean | Yes |

### Result
- **Description:** Possible action result
- **Types:** text
<a name="application"></a>
```yaml
---
type: class
name: application
suite: BetterTouchTool Script Suite
---
```

## Class: application

**Description:** BTTs top level scripting object.

