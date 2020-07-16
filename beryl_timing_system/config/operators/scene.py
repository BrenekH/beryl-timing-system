from .base import ConfigOperatorBase
from pathlib import Path
from typing import Dict

class SceneConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self._scene_registry_file: Path = root_dir / "scene_registry.json"

		self._scenes_dir: Path = root_dir / "scenes"
		self._scenes_dir.mkdir(parents=True, exist_ok=True)

		self._default_scene_registry_obj = {
			"active_scene": "default",
			"scenes": {
				"default": {
					"name": "Default"
				}
			}
		}

		self._default_scene_name = "New Scene"

		self._scene_registry = self.load_json(self._scene_registry_file, self._default_scene_registry_obj)

		self.active_scene_id = self._scene_registry["active_scene"]
		self.scenes: Dict[str, Dict[str, str]] = self._scene_registry["scenes"]

	def commit(self):
		self._scene_registry["active_scene"] = self.active_scene_id
		self._scene_registry["scenes"] = self.scenes

		self.dump_json(self._scene_registry_file, self._scene_registry)

	def new_scene(self, uuid: str):
		if uuid in self.scenes:
			raise ValueError(f"UUID {uuid} already exists in the scene registry")
		
		self.scenes[uuid] = {
			"name": self._default_scene_name
		}

		self.commit()

		return self.scenes[uuid]["name"]

	def set_scene_name(self, uuid: str, new_name: str, no_commit=False) -> None:
		if uuid not in self.scenes:
			raise ValueError(f"UUID {uuid} doesn't exist in the scene registry")

		self.scenes[uuid]["name"] = new_name

		if not no_commit:
			self.commit()
	
	def get_scene_name(self, uuid: str) -> str:
		if uuid not in self.scenes:
			raise ValueError(f"UUID {uuid} doesn't exist in the scene registry")
	
		return self.scenes[uuid]["name"]

	def delete_scene(self, uuid: str, no_commit=False) -> str:
		if uuid not in self.scenes:
			raise ValueError(f"UUID {uuid} doesn't exist in the scene registry")

		del self.scenes[uuid]

		if not no_commit:
			self.commit()
