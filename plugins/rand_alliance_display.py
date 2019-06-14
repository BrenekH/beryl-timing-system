import pygame
from pathlib import Path

class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class
		self.requirements = ["display"]

		self.bracket_id = "test"

		self.now_playing_image = pygame.image.load(str(Path("./plugins/Assets/images/NowPlaying.png")))
		self.up_next_image = pygame.image.load(str(Path("./plugins/Assets/images/UpNext.png")))

	def register_listeners(self):
		self.parent_class.register_on_loop_listener(self.on_loop)

	def info(self):
		return {"name": "Random Alliance Display", "uuid": "zpaw.rand_alliance.display", "family_id": "zpaw.rand_alliance"}

	def on_loop(self):
		plugin_display = self.parent_class.get_plugin_display()
		plugin_display.fill((255, 255, 255))
		plugin_display_rect = plugin_display.get_rect()

		# TODO: Place the team numbers on the image
		now_playing_image_with_team = self.now_playing_image.copy()
		up_next_image_with_team = self.up_next_image.copy()

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