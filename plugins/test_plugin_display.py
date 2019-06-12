import pygame

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]

	def register_listeners(self):
		self.parent_class.register_on_loop_listener(self.plugin_display)

	def info(self):
		return {"name": "Test Plugin Display", "uuid": "zpaw.test_game.test_display", "family_id": "zpaw.test_game"}

	def plugin_display(self):
		display = self.parent_class.get_plugin_display()
		display.fill((255, 255, 255))