import pygame
from .colors import Color
from .timer import Timer

class CoreDisplay:
	def __init__(self):
		self.running = False

		self.display = None
		self.clock = None
		
		self.width, self.height = (1280, 720)

		self.timer = None

	def start(self):
		pygame.init()
		self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		self.timer = Timer().load_settings()

		self.running = True
		self.__run__()

	def __run__(self):
		while self.running:
			self.display.fill(Color.white.value)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_SPACE:
						if self.timer.timer_running:
							self.timer.stop()
						else:
							self.timer.start()
				elif event.type == pygame.VIDEORESIZE:
					self.height = event.h
					self.width = event.w
					self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

			self.message_to_screen(str(self.timer.get_status()), Color.black.value, 50, self.width/2, 25)

			pygame.display.update()
		pygame.quit()

	def message_to_screen(self, msg, color, size, x, y):
		font = pygame.font.SysFont('Arial', size)
		screen_text = font.render(msg, True, color)
		screen_rect = screen_text.get_rect()
		screen_rect.center = (x, y)
		self.display.blit(screen_text, screen_rect)
