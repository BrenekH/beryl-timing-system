from json import dump, load
from pathlib import Path

class ConfigOperatorBase:
	def dump_json(self, file: Path, to_dump):
		dump(to_dump, file.open("w"), indent=4)
		return to_dump

	def load_json(self, file: Path, default):
		if not file.exists():
			self.dump_json(file, default)
		return load(file.open())
