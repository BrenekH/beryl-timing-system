import pygame

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]

	def register_listeners(self):
		self.parent_class.register_on_loop_listener(self.on_loop)

	def info(self):
		return {"name": "Random Alliance Display", "uuid": "zpaw.rand_alliance.display", "family_id": "zpaw.rand_alliance"}

	def on_loop(self):
		pass