from typing import Tuple

def serialize_color(color_tuple: Tuple[int, int, int]) -> str:
	"""Converts tuple color to a str that can be saved

	Args:
		color_tuple (Tuple[int, int, int]): The color tuple to serialize

	Returns:
		str: The serialized str
	"""
	r, g, b = color_tuple
	return f"rgb({r},{g},{b})"

def parse_color(color_str: str) -> Tuple[int, int, int]:
	"""Converts a string color into a tuple color

	Args:
		color_str (str): The string color to parse

	Returns:
		Tuple[int, int, int]: The parsed tuple color
	"""
	r, g, b = color_str.replace("rgb(", "").replace(")", "").replace(" ", "").split(",")
	return (int(r), int(g), int(b))
