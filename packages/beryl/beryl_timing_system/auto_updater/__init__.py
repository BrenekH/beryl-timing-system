import os
from semver import match
from .github_things import Repository

def check_for_update():
	# Return true if server version is greater than current version
	# TODO: Read current installed version from ../__init__.py
	return match("0.0.0", f'<{Repository("zPaw", "beryl-timing-system").get_latest_tag()}')
