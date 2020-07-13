from beryl_timing_system.config.operators.scene import SceneConfigOperator
from pathlib import Path

from .operators import DisplayConfigOperator, SceneConfigOperator

class ConfigCoordinator:
	"""Handles the instantiation of the ConfigOperators with the appropriate file paths
	"""
	def __init__(self):
		self.root_config_dir: Path = Path.home() / ".beryl-timing-system"
		self.root_config_dir.mkdir(parents=True, exist_ok=True)

		# ConfigOperators
		self._display_op = DisplayConfigOperator(self.root_config_dir)
		self._scene_op = SceneConfigOperator(self.root_config_dir)

	@property
	def display_config_operator(self):
		return self._display_op

	@property
	def scene_config_operator(self):
		return self._scene_op
