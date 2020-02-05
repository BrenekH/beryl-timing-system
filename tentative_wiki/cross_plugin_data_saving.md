# Cross Plugin Data
The Cross Plugin Data API allows plugins within a family to share non-persistent data between themselves.

## How to Use
The data is stored using key value pairs. To access the data, pass a key to `PluginManager.get_cross_plugin_data(self, key)`. Saving is done in a very similar way using `PluginManager.save_cross_plugin_data(self, key, value)`.

__Extended Example__

```python
class Plugin:
	def __init__(self, parent):
		self.parent = parent

	def get_my_data(self):
		self.parent.get_cross_plugin_data(self, "my_key")

	def save_my_data(self):
		self.parent.save_cross_plugin_data(self, "my_other_key", "my_data")
```
