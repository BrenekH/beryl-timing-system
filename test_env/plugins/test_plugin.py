import pygame
from beryl_plugin import PluginBase

class Plugin(PluginBase):
	def __init__(self, parent_class):
		PluginBase.__init__(self, parent_class, "Test", "zpaw.test_game.test", "zpaw.test_game")
		self.parent_class = parent_class
		self.requirements = []
		self.test_string = "Hello World"
		self.test_mutable = 0
		self.save_cross_plugin_data("mutable", self.test_mutable)

	def register_listeners(self):
		self.register_key_listener(pygame.K_a, self.test_key_listener)

	def test_key_listener(self):
		self.test_mutable += 1
		print(self.test_string + str(self.test_mutable))
		self.save_cross_plugin_data("mutable", self.test_mutable)