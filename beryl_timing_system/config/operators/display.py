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
