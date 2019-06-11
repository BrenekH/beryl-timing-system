import pygame

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]
		self.test_string = "Hello World"
		self.test_mutable = 0

	def register_listeners(self):
		self.parent_class.register_key_listener(pygame.K_a, self.test_key_listener)

	def info(self):
		return {"name": "Test", "uuid": "zpaw.test_game.test", "family_id": "zpaw.test_game"}

	def test_key_listener(self):
		self.test_mutable += 1
		print(self.test_string + str(self.test_mutable))