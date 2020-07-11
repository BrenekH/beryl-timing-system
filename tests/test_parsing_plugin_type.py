import pygame_menu
from beryl_timing_system.core.config.menu import SettingsMenu
from pytest import raises
from unittest.mock import Mock

# TODO: Expand tests to cover more edge cases

# Setup
settings_menu = SettingsMenu(Mock())

def parse_string(string: str):
	return settings_menu._parse_plugin_type(string)

def test_options_type():
	assert parse_string("options<One, 2, 3.0>") == (True, False, False, ["One", "2", "3.0"])
	assert parse_string("options <One, 2, 3.0>") == (True, False, False, ["One", "2", "3.0"])

def test_string_type():
	assert parse_string("string") == (False, False, False, pygame_menu.locals.INPUT_TEXT)

def test_password_type():
	assert parse_string("password") == (False, True, False, pygame_menu.locals.INPUT_TEXT)

def test_int_type():
	assert parse_string("int") == (False, False, False, pygame_menu.locals.INPUT_INT)

def test_float_type():
	assert parse_string("float") == (False, False, False, pygame_menu.locals.INPUT_FLOAT)

def test_color_type():
	assert parse_string("color<rgb>") == (False, False, True, "rgb")
	assert parse_string("color<hex>") == (False, False, True, "hex")

	with raises(AssertionError):
		assert parse_string("color<NaN>")
