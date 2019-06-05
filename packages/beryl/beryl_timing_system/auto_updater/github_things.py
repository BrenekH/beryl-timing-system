import os, requests, json

class Repository:
	def __init__(self, owner, repo_name, api_key):
		self.owner = owner
		self.repo_name = repo_name

	def get_latest_tag(self):
		# return "0.0.0"
		return json.loads(requests.get("https://api.github.com/repos/zPaw/kotlin-for-frc/releases/latest").text)["tag_name"]

	def get_resource_from_latest_release(self, resource_name, target_path):
		return "Not Implemented"
