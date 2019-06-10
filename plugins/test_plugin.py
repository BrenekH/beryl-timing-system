class Plugin:
	def __init__(self, parent_class):
		self.parent_class = parent_class

	def get_info(self):
		return {"name": "Test", "uuid": "zpaw.test_game.test", "family_id": "zpaw.test_game"}