import abc

class PluginBase(abc.ABC):
	def __init__(self, spawning_class, name, uuid, family_id):
		self._super_class = spawning_class
		self._child_name = name
		self._child_uuid = uuid
		self._child_family = family_id

	def info(self):
		return {"name": self._child_name, "uuid": self._child_uuid, "family_id": self._child_family}

	# Listeners
	def register_key_listener(self, key, listener):
		self._super_class.register_key_listener(key, listener)

	def register_period_change_listener(self, listener):
		self._super_class.register_period_change_listener(listener)

	def register_on_loop_listener(self, listener):
		self._super_class.register_on_loop_listener(listener)

	def get_cross_plugin_data(self, key):
		self._super_class.get_cross_plugin_data(self, key)

	def save_cross_plugin_data(self, key, value):
		self._super_class.save_cross_plugin_data(self, key, value)
