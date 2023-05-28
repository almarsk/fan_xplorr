import os
import sys
import subprocess

if not os.path.exists("config.json"):
    print("""Error: config file not found.
        Create file config.json with these contents:
            {"filename": "nodes"}""")
    sys.exit()

command =["venv\\Scripts\\python", "explore.py", "name", f"{sys.argv[1]}"]
subprocess.run(command, shell=True)
