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

		# API Requirements
		self.requested_requirements = []
		self.plugin_requirements = {"display": False}

	def load_plugins(self, plugins_to_load):
		# Use import_module to import the plugins in the provided list

		for plugin_name in plugins_to_load:
			# Import, create, and store Plugin Object
			plugin = import_module(plugin_name)
			pluginObject = plugin.Plugin(self)
			self.loaded_plugins[pluginObject.info()["uuid"]] = pluginObject

			# Register all of the plugin's requirements
			pluginObject.register_listeners()
			self.requested_requirements += pluginObject.requirements

		# Mark the needed API Requirements
		if "display" in self.requested_requirements:
			self.plugin_requirements["display"] = True

		print(f"{len(self.loaded_plugins)} plugins loaded")
		return self

	def need_game_display(self):
		return self.plugin_requirements["display"]

	def get_plugin_display(self):
		if self.parent_class.do_game_display:
			return self.parent_class.plugin_display
		else:
			raise ValueError("No plugins specified the need for the plugin display. Yet one tried to access it.")

	# Listeners
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

	def trigger_period_change_listeners(self, new_period, periods_left):
		for listener in self.period_change_listeners:
			listener(new_period, periods_left)

	def register_point_change_listener(self, listener):
		self.point_change_listeners.append(listener)

	def trigger_point_change_listeners(self):
		blue_points, red_points = (0, 0)
		for listener in self.point_change_listeners(self):
			# TODO: Actually grab points from the Core
			listener(blue_points, red_points)

	def register_on_interval_listener(self, interval_in_seconds, listener):
		if not interval_in_seconds in self.on_interval_listeners:
			self.on_interval_listeners[interval_in_seconds] = []
		self.on_interval_listeners[interval_in_seconds].append(listener)

	def trigger_on_interval_listeners(self):
		for listener in self.on_interval_listeners:
			listener()

	def register_on_loop_listener(self, listener):
		#! Do not use unless absolutely necessary
		self.on_loop_listeners.append(listener)

	def trigger_on_loop_listeners(self):
		for listener in self.on_loop_listeners:
			listener()
