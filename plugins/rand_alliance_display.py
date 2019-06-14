import pygame, socket, time, json
from pathlib import Path

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]

		self.bracket_id = "afternoon"
		self.cached_bracket = None
		self.last_bracket_update = 0

		TCP_IP, TCP_PORT = ("localhost", 1569)
		self.bufsize = 16384

		self.now_playing_image = pygame.image.load(str(Path("./plugins/Assets/images/NowPlaying.png")))
		self.up_next_image = pygame.image.load(str(Path("./plugins/Assets/images/UpNext.png")))

		self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.s.connect((TCP_IP, TCP_PORT))

		self.s.send("Hello".encode())
		print(self.s.recv(self.bufsize))

		time.sleep(0.5)
		self.s.send(f"chgbrkt{self.bracket_id}".encode())
		self.s.recv(self.bufsize)

	def register_listeners(self):
		self.parent_class.register_on_loop_listener(self.on_loop)

	def info(self):
		return {"name": "Random Alliance Display", "uuid": "zpaw.rand_alliance.display", "family_id": "zpaw.rand_alliance"}

	def on_loop(self):
		plugin_display = self.parent_class.get_plugin_display()
		plugin_display.fill((255, 255, 255))
		plugin_display_rect = plugin_display.get_rect()

		num_dict = self.get_match_team_numbers_from_server()

		# TODO: Get the team numbers from the server
		# now_playing_red_team1, now_playing_red_team2 = ("99", "98")
		# now_playing_blue_team1, now_playing_blue_team2 = ("9", "8")
		# up_next_red_team1, up_next_red_team2 = ("97", "96")
		# up_next_blue_team1, up_next_blue_team2 = ("7", "6")
		now_playing_red_team1, now_playing_red_team2 = (num_dict["nprt1"], num_dict["nprt2"])
		now_playing_blue_team1, now_playing_blue_team2 = (num_dict["npbt1"], num_dict["npbt2"])
		up_next_red_team1, up_next_red_team2 = (num_dict["unrt1"], num_dict["unrt2"])
		up_next_blue_team1, up_next_blue_team2 = (num_dict["unbt1"], num_dict["unbt2"])

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
		# Return dict with nprt1, nprt2, npbt1, npbt2, unrt1, unrt2, unbt1, unbt2
		return_dict = {}
		full_bracket = self.get_bracket_from_server()

		last_match_completed = 0
		for match_id in full_bracket["matches"]:
			if full_bracket["matches"][match_id]["complete"]:
				last_match_completed = int(match_id)

		np_match = str(last_match_completed + 1)
		try:
			return_dict["nprt1"], return_dict["nprt2"] = (str(full_bracket["matches"][np_match]["team1"][0]), str(full_bracket["matches"][np_match]["team1"][1]))
			return_dict["npbt1"], return_dict["npbt2"] = (str(full_bracket["matches"][np_match]["team2"][0]), str(full_bracket["matches"][np_match]["team2"][1]))
		except Exception as e:
			print(str(e))
			return_dict["nprt1"], return_dict["nprt2"] = ("", "")
			return_dict["npbt1"], return_dict["npbt2"] = ("", "")

		un_match = str(last_match_completed + 2)
		try:
			return_dict["unrt1"], return_dict["unrt2"] = (str(full_bracket["matches"][un_match]["team1"][0]), str(full_bracket["matches"][un_match]["team1"][1]))
			return_dict["unbt1"], return_dict["unbt2"] = (str(full_bracket["matches"][un_match]["team2"][0]), str(full_bracket["matches"][un_match]["team2"][1]))
		except Exception as e:
			print(str(e))
			return_dict["unrt1"], return_dict["unrt2"] = ("", "")
			return_dict["unbt1"], return_dict["unbt2"] = ("", "")

		return return_dict

	def get_bracket_from_server(self):
		if not self.last_bracket_update < int(time.time() - 4):
			return self.cached_bracket
		else:
			self.s.send("gbifullbracket".encode())
			self.cached_bracket = json.loads(self.s.recv(self.bufsize).decode('utf-8'))
			self.last_bracket_update = int(time.time())
			return self.cached_bracket
		
