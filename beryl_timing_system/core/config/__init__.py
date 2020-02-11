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
	
	def get_config(self, config_name: str):
		return None

	def save_config(self, config_name: str, config_content: str, overwrite: bool):
		return None

	
	# single plugin config methods
	def get_plugin_config(self, plugin_id: str, config_id: int):
		return None

	def get_current_plugin_config(self, plugin_id: str):
		return None

	def list_plugin_configs(self, plugin_id: str):
		return None

	def save_plugin_config(self, plugin_id: str, config_name: str, config_content: str, overwrite:bool=False):
		return None


	# family config methods
	def get_plugin_family_config(self, family_id: str, config_id: int):
		return None

	def get_current_plugin_family_config(self, family_id: str):
		return None

	def list_plugin_family_configs(self, family_id: str):
		return None

	def save_plugin_family_config(self, family_id: str, config_name: str, config_content: str, overwrite:bool=False):
		return None


	# main config methods
	def get_main_config(self, config_id: int):
		return None

	def get_current_main_config(self):
		return None

	def list_main_configs(self):
		return None

	def save_main_config(self, config_name: str, config_content: str, overwrite:bool=False):
		return None


	# timer config methods
	def get_timer_config(self, config_id: int):
		return None

	def get_current_timer_config(self):
		return None

	def list_timer_configs(self):
		return None

	def save_timer_config(self, config_name: str, config_content: str, overwrite:bool=False):
		return None
