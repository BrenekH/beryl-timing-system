import pygame_menu
from typing import Dict

class ScenesMenu:
	def __init__(self, parent, theme):
		self.parent = parent
		self.__theme = theme

		self._fullscreen_value: bool = None
		self._width_value: int = None
		self._height_value: int = None

		self.menu: pygame_menu.Menu = None

	def _create_base_menu(self, title) -> pygame_menu.Menu:
		return pygame_menu.Menu(title=title,
						 width=self.parent.width,
						 height=self.parent.height,
						 enabled=False,
						 theme=self.__theme,
						 onclose=pygame_menu.events.BACK)

	def generate(self) -> pygame_menu.Menu:
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

	def _create_plugin_menu(self, plugin_name, plugin_type_dict: Dict[str, str]) -> pygame_menu.Menu:
		menu = self._create_base_menu(plugin_name)
		return menu
