import os
import sys
import subprocess



if not os.path.exists("venv"):
    print("""Error: Virtual environment 'venv' not found.
        Run 'python3 wizard.py'""")
    sys.exit()

command = ["venv\\Scripts\\python explore.py", "make", f"{' '.join(sys.argv[1:])}"]
subprocess.run(command, shell=True)
