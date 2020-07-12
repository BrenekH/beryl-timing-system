import pygame_menu
from .manager import Event, PluginManager
from typing import Tuple

def parse_plugin_config_type(type_string: str) -> Tuple[bool, bool, str]:
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
