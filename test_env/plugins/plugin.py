from beryl_plugin import PluginBase
from beryl_plugin.listeners import beryl_plugin, on_key

@beryl_plugin
class Plugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Test", "zpaw.test_game.test")
		self.parent_class = parent_class
		self.requirements = []
		self.test_string = "Hello World"
		self.test_mutable = 0

	def stop(self):
		return None, self

	@on_key("a")
	def test_key_listener(self, key):
		self.test_mutable += 1
		print(self.test_string + str(self.test_mutable))

	@on_key("*")
	def test_all_key_listener(self, key):
		print(f"All keys {key}")
		return self
