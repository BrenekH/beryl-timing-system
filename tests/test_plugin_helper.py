from beryl_plugin import PluginBase

class MockPluginSuperClass:
	def __init__(self):
		self.key_listener_triggered = False
		self.period_change_triggered = False
		self.on_loop_triggered = False
		self.get_plugin_data_triggered = False
		self.set_plugin_data_triggered = False

	def reset(self):
		self.key_listener_triggered = False
		self.period_change_triggered = False
		self.on_loop_triggered = False
		self.get_plugin_data_triggered = False
		self.set_plugin_data_triggered = False

	# Listeners
	def register_key_listener(self, key, listener):
		self.key_listener_triggered = True

	def register_period_change_listener(self, listener):
		self.period_change_triggered = True

	def register_on_loop_listener(self, listener):
		self.on_loop_triggered = True

	def get_cross_plugin_data(self, child, key):
		self.get_plugin_data_triggered = True

	def save_cross_plugin_data(self, child, key, value):
		self.set_plugin_data_triggered = True

# Listener plugins
class KeyListenerPlugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Test", "zpaw.test_game.test", "zpaw.test_game")
		self.parent_class = parent_class
		self.requirements = []
		self.test_mutable = 0

	def register_listeners(self):
		self.register_key_listener(17, self.listener)

	def listener(self):
		self.test_mutable += 1

class PeriodListenerPlugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Test", "zpaw.test_game.test", "zpaw.test_game")
		self.parent_class = parent_class
		self.requirements = []
		self.test_mutable = 0

	def register_listeners(self):
		self.register_period_change_listener(self.listener)

	def listener(self):
		self.test_mutable += 1

class LoopListenerPlugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Test", "zpaw.test_game.test", "zpaw.test_game")
		self.parent_class = parent_class
		self.requirements = []
		self.test_mutable = 0

	def register_listeners(self):
		self.register_on_loop_listener(self.listener)

	def listener(self):
		self.test_mutable += 1

class SaveCrossPluginDataPlugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Save Cross Plugin Data", "zpaw.test_cpd.save", "zpaw.test_cpd")
		self.parent_class = parent_class
		self.requirements = []
		self.save_cross_plugin_data("my_key", "my_value")

class GetCrossPluginDataPlugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Get Cross Plugin Data", "zpaw.test_cpd.get", "zpaw.test_cpd")
		self.parent_class = parent_class
		self.requirements = []
		self.get_cross_plugin_data("my_key")

mockSuperClass = MockPluginSuperClass()

# Listener plugin instances
keyListenerPlugin = KeyListenerPlugin(mockSuperClass)
periodListenerPlugin = PeriodListenerPlugin(mockSuperClass)
loopListenerPlugin = LoopListenerPlugin(mockSuperClass)

class TestCallListeners:
	def test_call_register_key_listener(self):
		mockSuperClass.reset()
		keyListenerPlugin.register_listeners()
		assert mockSuperClass.key_listener_triggered == True

	def test_call_register_period_change_listener(self):
		mockSuperClass.reset()
		periodListenerPlugin.register_listeners()
		assert mockSuperClass.period_change_triggered == True

	def test_call_register_on_loop_listener(self):
		mockSuperClass.reset()
		loopListenerPlugin.register_listeners()
		assert mockSuperClass.on_loop_triggered == True

class TestCallCrossPluginData:
	def test_call_save_cross_plugin_data(self):
		mockSuperClass.reset()
		SaveCrossPluginDataPlugin(mockSuperClass)
		assert mockSuperClass.set_plugin_data_triggered == True

	def test_call_get_cross_plugin_data(self):
		mockSuperClass.reset()
		GetCrossPluginDataPlugin(mockSuperClass)
		assert mockSuperClass.get_plugin_data_triggered == True
