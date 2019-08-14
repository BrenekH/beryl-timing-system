# Checks for the basic file and folders needed for operation and creates them if they are missing.
from os import mkdir
from pathlib import Path

def check_required_folders():
    return (check_for_configs(), check_for_plugins(), check_for_sounds())

def check_for_configs():
    return check_for_and_create_folder(f"configs")

def check_for_plugins():
    return check_for_and_create_folder(f"plugins")

def check_for_sounds():
    return check_for_and_create_folder(f"sounds")

def check_for_and_create_folder(path: str):
    configs_dir = Path(path)
    if not configs_dir.is_dir():
        mkdir(str(configs_dir))
        print("Made new dir")
    return True