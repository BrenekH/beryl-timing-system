from pathlib import Path
from os import getenv

class ConfigManager:
	def __init__(self, directory: str=None):
		# Directory Management
		if directory:
			self.__directory: Path = Path(directory)
		else:
			self.__directory: Path = Path(getenv('LOCALAPPDATA') / "beryl/data")
		self.__validate_directory()

	def __validate_directory(self):
		"""Ensures that all folders are properly created in the directory supplied to the class
		"""
		self.__directory.mkdir(parents=True, exist_ok=True)

class InternalConfigManager:
	def __init__(self, config_manager: ConfigManager):
		self.__config_manager = config_manager

	def get_timer_config(self):
		pass

	def set_timer_config(self):
		pass

	def get_main_config(self):
		pass

	def set_main_config(self):
		pass

class ExternalConfigManager:
	def __init__(self, config_manager: ConfigManager):
		self.__config_manager = config_manager
