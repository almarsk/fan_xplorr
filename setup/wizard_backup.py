import subprocess
import platform
import json
import sys

def stop_auto_setup(err, gen_err):
    print("***",err,"***")
    print("***",gen_err,"***")
    sys.exit()

with open("setup/setup_steps.json", "r") as i:
    installation = json.load(i)

# TODO - get type of platform and add platform specific commands in setup_steps.json
if platform.system() != 'Darwin' and platform.system() != 'Linux':
    stop_auto_setup("this autosetup only works on mac os and linux", installation["error"])

# installation steps loop based on setup/setup_steps.json
for step in installation["steps"]:

    command = step["command"] # .get(platform, step["command"])
    if subprocess.run(command).returncode != 0:
        stop_auto_setup(step["error"], installation["error"])

print(installation["success"])
