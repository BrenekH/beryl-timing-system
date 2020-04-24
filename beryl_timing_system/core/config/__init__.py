from colorama import Fore
from json import dump
from os import getenv
from pathlib import Path
from random import choice
from string import ascii_letters
from typing import List

""" Data dir setup
root:
	scene_registry.json
	display.json
	scenes:
		random.json
	timer:
		random.json
	plugins:
		plugin1:
			random.json
		plugin2:
			random.json
"""

# Sample scene_registry.json
{
	"random" : {
		"uuid": "random",
		"name": "Scene 1"
	}, 
	"otherI" : {
		"uuid": "otherI",
		"name": "Scene 2"
	}
}

# Sample scene.json
{
	"name": "Scene 1",
	"uuid": "random",
	"layout": "normal",
	"plugins": [
		"game_map",
		"in_between_bracket"
	]
}

class SceneManager:
	registry_file_name = "scene_registry.json"

	def __init__(self, directory: str=None):
		# Instance vars
		self._registry = {}

		# Directory management
		if directory:
			self.__dir: Path = Path(directory)
		else:
			self.__dir: Path = Path(getenv('LOCALAPPDATA') / "beryl/data")
		self.__validate_directory()

		self.__setup_data_dirs()

	def __validate_directory(self, rel_dir: str=None):
		"""Ensures that all folders are properly created in the directory supplied to the class
		"""
		if rel_dir:
			(self.__dir / rel_dir).mkdir(parents=True, exist_ok=True)
		else:
			self.__dir.mkdir(parents=True, exist_ok=True)

	def __validate_file(self, rel_file_path: str, to_write:str=""):
		"""Checks for a file in the relative file path and if file doesn't exist, writes to_write to the file
		"""
		full_path = self.__dir / rel_file_path

		if not full_path.is_file() and not full_path.is_dir():
			with open(full_path, "w") as f:
				f.write(to_write)

	def __check_for_file(self, rel_file_path: str) -> bool:
		"""Checks for a file in the relative file path
		"""
		full_path = self.__dir / rel_file_path

		if not full_path.is_file() and not full_path.is_dir():
			return False
		
		return True

	def __setup_data_dirs(self):
		# Directories
		self.__validate_directory("scenes")
		self.__validate_directory("timer")
		self.__validate_directory("plugins")

		# Files
		if not self.__check_for_file(registry_file_name):
			self.new_scene()
			self.save_registry()

	def new_scene(self, scene_name="New Scene"):
		loop_counter = 0
		new_uuid = ""
		while True:
			new_uuid = self.__random_uuid()

			if new_uuid not in self._registry:
				break

			if loop_counter > 200:
				print(f"{Fore.RED}Unable to generate new UUID after 200 tries{Fore.RESET}")
				break
			loop_counter += 1
		
		return None
		
		self._registry[new_uuid] = {"uuid": new_uuid, "name": scene_name}

		self.save_scene(new_uuid, {"name": scene_name, "uuid": new_uuid, "layout": "normal", "plugins": []})

		# TODO: Generate blank timer json

	def __random_uuid(self) -> str:
		"""Generate a random string with the combination of lowercase and uppercase letters"""
		return "".join(choice(ascii_letters) for _ in range(8))

	def save_registry(self):
		dump(self._registry, self.__dir / registry_file_name)

	def validate_plugin_folders(self, plugin_ids: List[str]):
		# TODO: Loop through plugin_ids and validate directory on their name and plugins folder
		pass

	def save_scene(self, scene_uuid, scene_json):
		dump(scene_json, self.__dir / f"scenes/{scene_uuid}.json")
