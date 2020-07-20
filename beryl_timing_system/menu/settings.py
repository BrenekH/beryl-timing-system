import pygame, pygame_menu
from ..colors import Color
from .display_menu import DisplayMenu
from ..plugin_manager import parse_plugin_config_type
from .scenes_menu import ScenesMenu

class SettingsMenu:
	# This Settings menu is going to be crazy
	___layout = """
Main:
	Display:
		- Fullscreen toggle (button)
		- Default resolution (2 numerical entry)
		- 'Apply' (button)
	Scenes:
		- Set Active Scene (button to menu)
			- All existing scene names as buttons that set it to active
		- New Scene (button)
		- All existing scenes (as many buttons as it takes, including scrolling)
		Scene Menu:
			- Name (text entry)
			- Timer (button):
				- Early Stop Sound (button)
					Sound Menu:
						- Drop down [Not sure how this will be implemented]
						- Select your own (button)
				- Stop Sound (button)
					Sound Menu:
						- Drop down [Not sure how this will be implemented]
						- Select your own (button)
				- Idle Period (button)
				- 'Add Timing Period' (button)
				- All timing periods [in timing order] (many buttons)
					Timing Period Menu:
						- Name
						- Sequence number
						- Start time [seconds]
						- Duration [seconds]
						- Start sound
							Sound Menu:
								- Drop down [Not sure how this will be implemented]
								- Select your own (button)
			- Plugins (button):
				- Plugin (button)
				- All selected plugins (many buttons)
				Plugin Menu:
					- Plugin configuration as parsed
			- 'Delete Scene' (button)
			- 'Save' (button)
"""
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

	def _setup_menu(self):
		self.main_menu.add_button("Display Settings", DisplayMenu(self.parent, self.__theme).generate())

		self.main_menu.add_button("Scenes", ScenesMenu(self.parent, self.__theme).generate())
