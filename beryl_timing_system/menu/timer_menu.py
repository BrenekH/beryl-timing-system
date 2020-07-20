import pygame_menu

from .scenes_menu import random_uuid

class TimerMenu:
	def __init__(self, uuid, parent, theme):
		self.uuid = uuid
		self.parent = parent

		self.__theme = theme

		self.menu = None
	
	def _create_base_menu(self, title) -> pygame_menu.Menu:
		return pygame_menu.Menu(title=title,
						 width=self.parent.width,
						 height=self.parent.height,
						 enabled=False,
						 theme=self.__theme,
						 onclose=pygame_menu.events.BACK)

	def generate(self):
		self.menu = self._create_base_menu("Timer Settings")
		self.menu.add_button("Early Stop Sound", self._create_sound_menu("Select Early Stop Sound"))
		self.menu.add_button("Stop Sound", self._create_sound_menu("Select Stop Sound"))
		# TODO: Add Idle Period menu
		# TODO: Add other periods in sequence order
		return self.menu

	def _create_sound_menu(self, title=""):
		"""Creates and returns a general menu for selecting sounds
		"""
		menu = self._create_base_menu(title)
		return menu

	def _create_period_menu(self):
		"""Creates and returns a general menu for configuring timing periods
		"""
		return

	def _add_period_menu(self):
		"""Button handler that creates a new timing period and adds it to the menu
		"""
		return

"""
Timer (button):
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
"""
