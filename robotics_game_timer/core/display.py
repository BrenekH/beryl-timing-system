import pygame

class CoreDisplay:
	def __init__(self):
		self.running = False
		self.display = None
		self.width, self.height = (100, 100)

	def start(self):
		self.display = pygame.display.set_mode((self.width, self.height), RESIZABLE)

		self.__run__()

	def __run__(self):
		pass