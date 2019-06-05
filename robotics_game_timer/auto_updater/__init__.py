import os
from .github_things import *

def check_for_update():
	print("Checking for updates")
	repo = Repository("zPaw", "kotlin-for-frc", os.getenv("GITHUB_THINGS_TOKEN"))
	print("Kotlin For FRC is at version: " + repo.get_latest_tag()[1])