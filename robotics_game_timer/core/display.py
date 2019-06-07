import pygame
from .colors import Color
from .timer import Timer

class CoreDisplay:
	def __init__(self):
		self.running = False
		self.do_game_display = False
		self.toggle_timer = False

		self.display = None
		self.clock = None
		
		self.width, self.height = (1280, 720)

		self.timer = None

	def start(self):
		pygame.init()
		self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		self.timer = Timer().ready_timer()

		# TODO: Load plugins and switch do_game_display accordingly

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
						self.toggle_timer = True
				elif event.type == pygame.VIDEORESIZE:
					self.height = event.h
					self.width = event.w
					self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)

			if self.toggle_timer:
				if self.timer.timer_running:
					self.timer.stop()
				else:
					self.timer.start()
				self.toggle_timer = False

			# TODO: Actually implement a game display surface
			timer_status = self.timer.get_status()
			if self.do_game_display:
				pass
			else:
				self.display.fill(timer_status[2])
				# self.message_to_screen(str(timer_status), timer_status[3], 50, self.width/2, 25)
				self.message_to_screen(str(timer_status[0]), timer_status[3], 50, self.width/2, (self.height/6) * 2) # Game Mode
				self.message_to_screen(str(timer_status[1]), timer_status[3], 50, self.width/2, (self.height/6) * 3) # Time Left

			pygame.display.update()
		pygame.quit()

	def message_to_screen(self, msg, color, size, x, y):
		font = pygame.font.SysFont('Arial', size)
		screen_text = font.render(msg, True, color)
		screen_rect = screen_text.get_rect()
		screen_rect.center = (x, y)
		self.display.blit(screen_text, screen_rect)
