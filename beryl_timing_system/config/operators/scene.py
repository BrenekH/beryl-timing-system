from .base import ConfigOperatorBase
from pathlib import Path

class SceneConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self.scene_registry_file: Path = root_dir / "scene_registry.json"

		self.scenes_dir: Path = root_dir / "scenes"
		self.scenes_dir.mkdir(parents=True, exist_ok=True)

		self.default_scene_registry_obj = {
			"active_scene": "default",
			"scenes": {
				"default" : {
					"name": "Scene 1"
				}
			}
		}

		self.scene_registry = self.load_json(self.scene_registry_file, self.default_scene_registry_obj)
