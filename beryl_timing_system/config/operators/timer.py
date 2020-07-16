from .base import ConfigOperatorBase
from pathlib import Path

class TimerConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self.default_timer_config = {}
