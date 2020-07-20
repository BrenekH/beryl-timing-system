from .base import ConfigOperatorBase
from pathlib import Path

class DisplayConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self._config_file: Path = root_dir / "display_config.json"

		self._default_display_obj = {
			"fullscreen": False,
			"resolution": {
				"width": 1280,
				"height": 720
			}
		}

		self._data_obj = self.load_json(self._config_file, self._default_display_obj)

		self.fullscreen: bool = self._data_obj["fullscreen"]
		self.width: int = self._data_obj["resolution"]["width"]
		self.height: int = self._data_obj["resolution"]["height"]

	def commit(self):
		"""Commit the current values in memory to the json file
		"""
		self._data_obj["fullscreen"] = self.fullscreen
		self._data_obj["resolution"]["width"] = self.width
		self._data_obj["resolution"]["height"] = self.height

		self.dump_json(self._config_file, self._data_obj)
