import subprocess
import platform
import json
import sys
import os

def stop_auto_setup(err, gen_err):
    print("***",err,"***")
    print("***",gen_err,"***")
    if os.path.exists("venv"):
        subprocess.run(["rm", "-rf", "venv"])
    sys.exit()

inst_type = ""

if platform.system() == 'Windows':
    inst_type = "_w"
elif platform.system() != 'Darwin' and platform.system() != 'Linux':
    stop_auto_setup("this autosetup only works on mac os and linux and windows", "consult documentation for manual installation")
with open(f"setup/setup_steps{inst_type}.json", "r") as i:
    installation = json.load(i)

# installation steps loop based on setup/setup_steps.json
for step in installation["steps"]:
    command = step["command"]
    print(" ".join(command))
    if subprocess.run(command).returncode != 0:
        stop_auto_setup(step["error"], installation["error"])

print(installation["success"])

os.remove("example.png")
os.remove(__file__)
