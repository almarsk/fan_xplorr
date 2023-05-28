import os
import fire
import subprocess

def main(*words):

    if not os.path.exists("venv"):
        return """Error: Virtual environment 'venv' not found.
           Run 'python3 wizard.py'"""

        command = f"venv\\Scripts\\activate && python explore.py make {' '.join(words)} && deactivate"
        subprocess.run(command, shell=True)

if __name__ == '__main__':
    fire.Fire(main)
