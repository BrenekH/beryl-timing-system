from importlib import import_module

class EventManager:
	def __init__(self, parent_class):
		self.parent_class = parent_class

		self.loaded_plugins = {}
		
		# Listener collections
		self.key_listeners = {}
		self.on_interval_listeners = {}
		self.period_change_listeners = []
		self.point_change_listeners = []
		self.on_loop_listeners = []

	def load_plugins(self, plugins_to_load):
		# Use import_module to import the plugins in the provided list

		for plugin_name in plugins_to_load:
			# Import, create, and store Plugin Object
			plugin = import_module(plugin_name)
			pluginObject = plugin.Plugin(self)
			self.loaded_plugins[pluginObject.info()["uuid"]] = pluginObject

			# Register all of the plugin's requirements
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

	def register_period_change_listener(self, listener):
		self.period_change_listeners.append(listener)

	def trigger_period_change_listeners(self):
		pass

	def register_point_change_listener(self, listener):
		self.point_change_listeners.append(listener)

	def trigger_point_change_listeners(self):
		pass

	def register_on_interval_listener(self, interval_in_seconds, listener):
		if not interval_in_seconds in self.on_interval_listeners:
			self.on_interval_listeners[interval_in_seconds] = []
		self.on_interval_listeners[interval_in_seconds].append(listener)

	def trigger_on_interval_listeners(self):
		pass

	def register_on_loop_listener(self, listener):
		# Do not use unless absolutely necessary
		self.on_loop_listeners.append(listener)

	def trigger_on_loop_listeners(self):
		for listener in self.on_loop_listeners:
			listener()
