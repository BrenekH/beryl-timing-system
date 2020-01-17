from pathlib import Path
from os import getenv

class ConfigManager:
	def __init__(self, directory: str=None):
		# Directory Management
		if directory:
			self.__directory: Path = Path(directory)
		else:
			self.__directory: Path = Path(getenv('LOCALAPPDATA') + "/beryl/data")
		self.__validate_directory()

	def __validate_directory(self):
		"""Ensures that all folders are properly created in the directory supplied to the class
		"""
		# TODO: Implement
		pass

class InternalConfigManager:
	def __init__(self, config_manager: ConfigManager):
		self.__config_manager = config_manager

class ExternalConfigManager:
	def __init__(self, config_manager: ConfigManager):
		self.__config_manager = config_manager
