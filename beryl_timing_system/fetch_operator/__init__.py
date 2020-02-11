import platform, os

class FetchOperator:
	def __init__(self):
		self.bit64_arch = True

		if platform.architecture()[0] == '32bit':
			self.bit64_arch = False

	def fetch_binary(self):
		if bit64_arch:
			return "fetch_windows_amd64.exe"
		else:
			return "fetch_windows_386.exe"

	def get_resource_from_repo(self, repo_url, tag, asset_name, github_oauth_token):
		return os.system(f"{self.fetch_binary()} --repo --tag --release-asset")