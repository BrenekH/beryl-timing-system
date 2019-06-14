import pygame, socket, time, json
from pathlib import Path

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]

		self.bracket_id = "test"
		self.cached_bracket = None
		self.last_bracket_update = 0

		TCP_IP, TCP_PORT = ("localhost", 1569)
		self.bufsize = 16384

		self.now_playing_image = pygame.image.load(str(Path("./plugins/Assets/images/NowPlaying.png")))
		self.up_next_image = pygame.image.load(str(Path("./plugins/Assets/images/UpNext.png")))

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((TCP_IP, TCP_PORT))

		self.s.send("Hello".encode())
		self.s.recv(self.bufsize)

		self.s.send(f"chgbrkt{self.bracket_id}")

	def register_listeners(self):
		self.parent_class.register_on_loop_listener(self.on_loop)

	def info(self):
		return {"name": "Random Alliance Display", "uuid": "zpaw.rand_alliance.display", "family_id": "zpaw.rand_alliance"}

	def on_loop(self):
		plugin_display = self.parent_class.get_plugin_display()
		plugin_display.fill((255, 255, 255))
		plugin_display_rect = plugin_display.get_rect()

		self.get_bracket_from_server()

		# TODO: Get the team numbers from the server
		now_playing_red_team1, now_playing_red_team2 = ("99", "98")
		now_playing_blue_team1, now_playing_blue_team2 = ("9", "8")
		up_next_red_team1, up_next_red_team2 = ("97", "96")
		up_next_blue_team1, up_next_blue_team2 = ("7", "6")

		# Place numbers on the screen
		now_playing_image_with_team = self.now_playing_image.copy()
		up_next_image_with_team = self.up_next_image.copy()

		self.message_to_surface(now_playing_image_with_team, now_playing_red_team1, (255, 0, 0), 100, 250, 450)
		self.message_to_surface(now_playing_image_with_team, now_playing_red_team2, (255, 0, 0), 100, 250, 650)

		self.message_to_surface(now_playing_image_with_team, now_playing_blue_team1, (0, 0, 255), 100, 750, 450)
		self.message_to_surface(now_playing_image_with_team, now_playing_blue_team2, (0, 0, 255), 100, 750, 650)

		self.message_to_surface(up_next_image_with_team, up_next_red_team1, (255, 0, 0), 100, 250, 450)
		self.message_to_surface(up_next_image_with_team, up_next_red_team2, (255, 0, 0), 100, 250, 650)

		self.message_to_surface(up_next_image_with_team, up_next_blue_team1, (0, 0, 255), 100, 750, 450)
		self.message_to_surface(up_next_image_with_team, up_next_blue_team2, (0, 0, 255), 100, 750, 650)

		# Scale the rects
		target_side_length = int(plugin_display_rect.height * .75)
		now_playing_transform = pygame.transform.scale(now_playing_image_with_team, (target_side_length, target_side_length))
		up_next_transform = pygame.transform.scale(up_next_image_with_team, (target_side_length, target_side_length))

		# Position the Rects
		now_playing_rect = now_playing_transform.get_rect()
		up_next_rect = up_next_transform.get_rect()
		now_playing_rect.center = (plugin_display_rect.width/4, plugin_display_rect.height/2)
		up_next_rect.center = (plugin_display_rect.width - plugin_display_rect.width/4, plugin_display_rect.height/2)

		plugin_display.blit(now_playing_transform, now_playing_rect)
		plugin_display.blit(up_next_transform, up_next_rect)

	def message_to_surface(self, surface, msg, color, size, x, y):
		font = pygame.font.SysFont('Arial', size)
		screen_text = font.render(msg, True, color)
		screen_rect = screen_text.get_rect()
		screen_rect.center = (x, y)
		surface.blit(screen_text, screen_rect)

	def message_to_surface_top_left(self, surface, msg, color, size, x, y):
		font = pygame.font.SysFont('Arial', size)
		screen_text = font.render(msg, True, color)
		surface.blit(screen_text, (x, y))

	def get_match_team_numbers_from_server(self):
		# Return dict with nprt1, nprt2, npbt1, npbt2, uprt1, uprt2, upbt1, upbt2
		return_dict = {}

		return return_dict

	def get_bracket_from_server(self):
		if not self.last_bracket_update < int(time.time() - 1):
			return self.cached_bracket
		else:
			self.s.send("gbifullbracket".encode())
			self.cached_bracket = json.loads(self.s.recv(self.bufsize).decode('utf-8'))
			print(self.cached_bracket)
			return self.cached_bracket
		
