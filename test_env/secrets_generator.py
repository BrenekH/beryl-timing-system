import os

with open("secrets.py", "w") as f:
	f.write(f"""
GITHUB_API_TOKEN = \"{os.getenv("GITHUB_API_TOKEN")}\"
	""")