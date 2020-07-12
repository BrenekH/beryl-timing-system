import pygame, pygame_menu
from typing import Dict, Tuple
from ..colors import Color

class SettingsMenu:
	def __init__(self, parent):
		self.parent = parent

		self.__theme = pygame_menu.themes.THEME_DARK

	def start(self):
		"""Initializes all required code and repeatedly calls the self.__loop function
		"""

		# Make sure that the user can't screw up the menu by resizing the window
		pygame.display.set_mode((self.parent.width, self.parent.height))

		self.main_menu = self._create_base_menu("Settings")

		self._setup_menu()

		self.main_menu.enable()

		while True:
			if self.__loop():
				# self.__loop returns True when no more menus are enabled
				break

		# Re-enable the ability to resize the window
		pygame.display.set_mode((self.parent.width, self.parent.height), pygame.RESIZABLE)

	def __loop(self):
		"""Performs one "loop" of the code required to run the menus
		"""
		self.parent.display.fill(Color.black.value)

		events = pygame.event.get()
		if self.main_menu.is_enabled():
			self.main_menu.update(events)

		if self.main_menu.is_enabled():
			self.main_menu.draw(self.parent.display)

		pygame.display.update()

		return not self.main_menu.is_enabled()

	def _create_base_menu(self, title) -> pygame_menu.Menu:
		return pygame_menu.Menu(title=title,
						 width=self.parent.width,
						 height=self.parent.height,
						 enabled=False,
						 theme=self.__theme,
						 onclose=pygame_menu.events.BACK)

	def _create_plugin_menu(self, plugin_name, plugin_type_dict: Dict[str, str]) -> pygame_menu.Menu:
		menu = self._create_base_menu("Title")
		return menu

	def _setup_menu(self):
		self.main_menu.add_button("Display Settings", self._create_display_settings_menu())

		self.main_menu.add_button("Scenes", self._create_scenes_main_menu())

	def _create_display_settings_menu(self) -> pygame_menu.Menu:
		menu = self._create_base_menu("Display Settings")
		# TODO: Add fullscreen toggle
		# TODO: Add default resolution
		# TODO: 'Apply' button
		return menu

	def _create_scenes_main_menu(self) -> pygame_menu.Menu:
		menu = self._create_base_menu("Scenes")
		# TODO: Add 'New Scene' button
		# TODO: Add all existing scenes buttons
		return menu

	def _create_scene_menu(self, uuid=None, new=False) -> pygame_menu.Menu:
		# TODO: Perform uuid lookup if new is False
		menu = self._create_base_menu("Random Scene")
		# TODO: Add 'Timer' menu button
		# TODO: Add 'Plugins' menu button
		# TODO: Add 'Layout' selector
		return menu

def parse_plugin_type(type_string: str) -> Tuple[bool, bool, str]:
	# (options, password, color input, type to pass or extra data)
	type_string = type_string.strip()

	if type_string.startswith("options"):
		options_str = type_string.split("<")[1].split(">")[0]

		options_list = []
		for option in options_str.split(","):
			if option.startswith(" "):
				options_list.append(option[1:].strip())
			else:
				options_list.append(option.strip())

		return (True, False, False, options_list)
	elif type_string.startswith("color"):
		color_type = type_string.split("<")[1][:-1]

		assert color_type == "rgb" or color_type == "hex", "Color type must be 'rgb' or 'hex'"

		return (False, False, True, color_type)
	elif type_string == "password":
		return (False, True, False, pygame_menu.locals.INPUT_TEXT)
	elif type_string == "int":
		return (False, False, False, pygame_menu.locals.INPUT_INT)
	elif type_string == "float":
		return (False, False, False, pygame_menu.locals.INPUT_FLOAT)

	return (False, False, False, pygame_menu.locals.INPUT_TEXT)
