import os
from semver import match
from .github_things import Repository
from .. import version as software_version

def check_for_update():
	# Return true if server version is greater than current version
	return match(software_version, f'<{Repository("zPaw", "beryl-timing-system").get_latest_tag()}')
