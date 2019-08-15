# Main entry point
if __name__ == "__main__":
	import secrets
	from beryl_timing_system import auto_updater
	from beryl_timing_system import core
	from beryl_timing_system import file_path_integrity
	auto_updater.check_for_update()												#api_key=secrets.GITHUB_THINGS_TOKEN)
	print(file_path_integrity.check_required_folders())
	display = core.CoreDisplay()
	display.start()