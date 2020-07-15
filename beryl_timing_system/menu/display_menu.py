import pygame_menu

class DisplayMenu:
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
		menu = self._create_base_menu("Display Settings")
		# Add fullscreen toggle
		current_value = self.parent.config_coordinator.display_config_operator.fullscreen
		self._fullscreen_value = current_value
		menu.add_selector("Fullscreen: ", [("False", False), ("True", True)], default=translate_bool_to_index(current_value), onchange=self.fullscreen_on_change)
		
		menu.add_vertical_margin(30)

		# Add default resolution
		menu.add_label("Default Resolution")
		menu.add_vertical_margin(10)
		
		current_value = self.parent.config_coordinator.display_config_operator.width
		self._width_value = current_value
		menu.add_text_input("Width(x): ", default=str(current_value), input_type=pygame_menu.locals.INPUT_INT, onchange=self.width_on_change)

		current_value = self.parent.config_coordinator.display_config_operator.height
		self._height_value = current_value
		menu.add_text_input("Height(y): ", default=str(current_value), input_type=pygame_menu.locals.INPUT_INT, onchange=self.height_on_change)
		
		menu.add_vertical_margin(50)

		# 'Apply' button
		menu.add_button("Save", self.apply_on_click)
		menu.add_label("Changes will not take effect until the settings menu is closed")

		self.menu = menu
		return menu
		
	def fullscreen_on_change(self, _, value: bool):
		self._fullscreen_value = value

	def width_on_change(self, value: int):
		self._width_value = int(value)

	def height_on_change(self, value: int):
		self._height_value = int(value)

	def apply_on_click(self):
		if self._fullscreen_value == None or self._width_value == None or self._height_value == None:
			raise ValueError(f"One of the values to be saved to display_config.json was None. F{self._fullscreen_value} W{self._width_value} H{self._height_value}")
		
		self.parent.config_coordinator.display_config_operator.fullscreen = self._fullscreen_value
		self.parent.config_coordinator.display_config_operator.width = self._width_value
		self.parent.config_coordinator.display_config_operator.height = self._height_value
		
		self.parent.config_coordinator.display_config_operator.commit()

		self.menu.full_reset()

def translate_bool_to_index(value: bool) -> int:
	if value:
		return 1
	else:
		return 0
