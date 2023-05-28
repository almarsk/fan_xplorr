import os
import fire
import subprocess

def main(word):

    if not os.path.exists("config.json"):
        return """Error: config file not found.
           Create file config.json with these contents:
               {"filename": "nodes"}"""

        command = f"venv\\Scripts\\activate && python explore.py name {word} && deactivate"
        subprocess.run(command, shell=True)

if __name__ == '__main__':
    fire.Fire(main)
