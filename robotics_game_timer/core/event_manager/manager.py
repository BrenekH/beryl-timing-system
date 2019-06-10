from importlib import import_module

class EventManager:
	def __init__(self, parent_class):
		self.parent_class = parent_class

		self.loaded_plugins = {}
		
		self.key_listeners = {}	

	def load_plugins(self, plugins_to_load):
		# Use import_module to import the plugins in the provided list

		for plugin_name in plugins_to_load:
			# Import, create, and store Plugin Object
			plugin = import_module(plugin_name)
			pluginObject = plugin.Plugin(self)
			self.loaded_plugins[pluginObject.info()["uuid"]] = pluginObject

			# Register all of the plugins requirements
			pluginObject.register_listeners()

		print(f"{len(self.loaded_plugins)} plugins loaded")
		return self

	def register_key_listener(self, key, listener):
		if not key in self.key_listeners:
			self.key_listeners[key] = []
		self.key_listeners[key].append(listener)

	def trigger_key_listeners(self, key_triggered):
		if not key_triggered in self.key_listeners:
			return False
		for key in self.key_listeners:
			if key == key_triggered:
				for listener in self.key_listeners[key]:
					listener()
				break

		return True
