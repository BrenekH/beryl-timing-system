from .base import ConfigOperatorBase
from pathlib import Path

class DisplayConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self.config_file: Path = root_dir / "display_config.json"

		self.default_display_obj = {
			"fullscreen": False,
			"resolution": {
				"width": 1280,
				"height": 720
			}
		}

		self.data_obj = self.load_json(self.config_file, self.default_display_obj)

		self.fullscreen: bool = self.data_obj["fullscreen"]
		self.width: int = self.data_obj["resolution"]["width"]
		self.height: int = self.data_obj["resolution"]["height"]

	def commit(self):
		"""Commit the current values in memory to the json file
		"""
		self.data_obj["fullscreen"] = self.fullscreen
		self.data_obj["resolution"]["width"] = self.width
		self.data_obj["resolution"]["height"] = self.height

		self.dump_json(self.config_file, self.data_obj)
