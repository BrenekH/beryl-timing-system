# Main entry point
if __name__ == "__main__":
	import secrets
	# from robotics_game_timer import auto_updater
	from robotics_game_timer import core
	# auto_updater.check_for_update(api_key=secrets.GITHUB_THINGS_TOKEN)
	display = core.CoreDisplay()
	display.start()