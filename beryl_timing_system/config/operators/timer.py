from .base import ConfigOperatorBase
from pathlib import Path
from ...util import parse_color, serialize_color

class TimerConfigOperator(ConfigOperatorBase):
	def __init__(self, root_dir: Path):
		self.root_dir = root_dir

		self.default_timer_config = {
			"timing_periods": {
				"idDefault": {
					"name": "Default",
					"text": "",
					"sequence": 1,
					"start_time": 0,
					"duration": 60,
					"background_color": serialize_color((128, 0, 0)),
					"foreground_color": serialize_color((255, 255, 255))
				}
			},
			"idle_period": {
				"text": "OFF",
				"background_color": serialize_color((0, 128, 0)),
				"foreground_color": serialize_color((255, 255, 255))
			},
			"early_stop_sound": "zPaw-bts-internal/descending-foghorn.wav",
			"stop_sound": "zPaw-bts-internal/buzzer.wav"
		}
