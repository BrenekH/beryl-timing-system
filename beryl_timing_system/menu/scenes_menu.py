import pygame_menu
from random import choice
from string import ascii_letters
from typing import Dict

class ScenesMenu:
	def __init__(self, parent, theme):
		self.parent = parent
		self.__theme = theme

		self._fullscreen_value: bool = None
		self._width_value: int = None
		self._height_value: int = None

		self.main_menu: pygame_menu.Menu = None

		self._tentative_name_store = None

	def _create_base_menu(self, title) -> pygame_menu.Menu:
		return pygame_menu.Menu(title=title,
						 width=self.parent.width,
						 height=self.parent.height,
						 enabled=False,
						 theme=self.__theme,
						 onclose=pygame_menu.events.BACK)

	def generate(self) -> pygame_menu.Menu:
		self.main_menu = self._create_base_menu("Scenes")
		# TODO: Add 'Set Active Scene' menu
		# Add 'New Scene' button
		self.main_menu.add_button("Create New Scene", self._new_scene_on_click)
		self.main_menu.add_vertical_margin(20)

		# Add all existing scenes buttons
		for uuid in self.parent.config_coordinator.scene_config_operator.scenes:
			scene = self.parent.config_coordinator.scene_config_operator.scenes[uuid]
			self.main_menu.add_button(scene["name"], self._create_scene_menu(uuid), button_id=uuid)

		return self.main_menu

	def _new_scene_on_click(self) -> pygame_menu.Menu:
		new_scene_uuid = self.generate_new_uuid()
		new_scene_name = self.parent.config_coordinator.scene_config_operator.new_scene(new_scene_uuid)
		self.main_menu.add_button(new_scene_name, self._create_scene_menu(new_scene_uuid), button_id=new_scene_uuid)

	def _create_scene_menu(self, uuid) -> pygame_menu.Menu:		
		if uuid not in self.parent.config_coordinator.scene_config_operator.scenes:
			raise ValueError(f"UUID {uuid} was not found in the scene registry")

		menu = self._create_base_menu("Scene Settings")
		# Add Name text entry
		menu.add_text_input("Name: ", default=self.parent.config_coordinator.scene_config_operator.get_scene_name(uuid), onchange=self._save_temp_scene_name_factory(uuid))
		
		# Add 'Timer' menu button
		menu.add_button("Timer", self._create_timer_menu(uuid))
		# TODO: Add 'Plugins' menu button
		# TODO: Add 'Layout' selector
		# Add 'Delete Scene' button
		menu.add_button("Delete Scene", self._delete_scene_factory(uuid, menu))
		# Add 'Save' button
		menu.add_button("Save", self._save_scene)
		return menu

	def _delete_scene_factory(self, uuid: str, current_menu: pygame_menu.Menu):
		def return_fun():
			self.parent.config_coordinator.scene_config_operator.delete_scene(uuid)
			self.main_menu.remove_widget(self.main_menu.get_widget(uuid))
			current_menu.reset(1)
		return return_fun

	def _save_scene(self):
		if self._tentative_name_store == None:
			return
		
		uuid, value = self._tentative_name_store

		self.parent.config_coordinator.scene_config_operator.set_scene_name(uuid, value)
		self.main_menu.get_widget(uuid).set_title(value)

		self._tentative_name_store = None

	def _save_temp_scene_name_factory(self, uuid):
		def return_func(value):
			self._tentative_name_store = (uuid, value)
		return return_func

	def _create_timer_menu(self, scene_uuid) -> pygame_menu.Menu:
		menu = self._create_base_menu("Timer Settings")
		return menu

	def _create_plugin_menu(self, plugin_name, plugin_type_dict: Dict[str, str]) -> pygame_menu.Menu:
		menu = self._create_base_menu(plugin_name)
		return menu

	def generate_new_uuid(self) -> str:
		loop_counter = 0
		new_uuid = ""
		while True:
			new_uuid = random_uuid()

			if new_uuid not in self.parent.config_coordinator.scene_config_operator.scenes:
				break

			if loop_counter > 200:
				print("Unable to generate new UUID after 200 tries")
				return None

			loop_counter += 1

		return new_uuid

def random_uuid() -> str:
	"""Generate a random string with the combination of lowercase and uppercase letters"""
	return "".join(choice(ascii_letters) for _ in range(16))

"""
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
			- 'Add Timing Period' (button)
		- Plugins (button):
			- Plugin (button)
			- All selected plugins (many buttons)
			Plugin Menu:
				- Plugin configuration as parsed
		- 'Delete Scene' (button)
		- 'Save' (button)
"""
