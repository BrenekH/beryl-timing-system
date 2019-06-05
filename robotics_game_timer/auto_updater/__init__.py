import os
from .github_things import *

def check_for_update(api_key=os.getenv("GITHUB_THINGS_TOKEN")):
	print("Checking for updates")
	repo = Repository("zPaw", "robotics-camp-game-timer", api_key)
	print("Robotics Camp Game Timer is at version: " + repo.get_latest_tag()[1])