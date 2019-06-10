from importlib import import_module

class EventManager:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.loaded_plugins = {}

	def load_plugins(self, plugins_to_load):
		# Use import_module to import the plugins in the provided list
		
		for plugin_name in plugins_to_load:
			plugin = import_module(plugin_name)
			pluginObject = plugin.Plugin(self)
			self.loaded_plugins[pluginObject.get_info()["uuid"]] = pluginObject

		return self