import pygame, json
from pathlib import Path
from .colors import Color
from .timer import Timer
from .event_manager import EventManager

class CoreDisplay:
	def __init__(self):
		self.running = False
		self.do_game_display = False
		self.toggle_timer = False

		self.display = None
		self.plugin_display = None
		self.clock = None
		
		self.width, self.height = (1280, 720)

		self.timer = None
		self.manager = None

		self.config = None

	def start(self):
		pygame.init()
		self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		self.load_config()

		self.timer = Timer().ready_timer()

		self.manager = EventManager(self)

		# TODO: Load plugins and switch do_game_display accordingly
		self.manager.load_plugins(self.config["active_plugins"])

		self.do_game_display = self.manager.need_game_display()

		if self.do_game_display:
			self.plugin_display = pygame.Surface((self.width, self.height - 100))

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
					self.manager.trigger_key_listeners(event.key)
				elif event.type == pygame.VIDEORESIZE:
					self.height = event.h
					self.width = event.w
					self.display = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
					
					if self.do_game_display:
						self.plugin_display = pygame.Surface((self.width, self.height - 100))

			if self.toggle_timer:
				if self.timer.timer_running:
					self.timer.stop()
				else:
					self.timer.start()
				self.toggle_timer = False

			# Listener triggering
			self.manager.trigger_on_loop_listeners()

			timer_status = self.timer.get_status()
			if self.do_game_display:
				pygame.draw.rect(self.display, timer_status[2], ((0, 0, self.width, 100)))
				self.message_to_screen(str(timer_status[0]), timer_status[3], 50, self.width/2, 25) # Game Mode
				self.message_to_screen(str(timer_status[1]), timer_status[3], 50, self.width/2, 75) # Time Left

				self.display.blit(self.plugin_display, (0, 100))
			else:
				self.display.fill(timer_status[2])
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

	def load_config(self, config_name="default.json"):
		self.config = json.load(open(Path(f"configs/main/{config_name}")))
