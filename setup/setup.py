import subprocess

if subprocess.run(["python", "setup/import_data.py"]).returncode == 0 and \
subprocess.run(["python", "setup/process_data_just_words.py"]).returncode == 0:
    print("""

    Welcome to USF Free associations network explorer!

    This is the command you want to run now:

    python explore.py make word of your choice

    You'll find the graphs in the "graphs" directory (it will be created with your first graph)
    If you want to change the name of the file you save your graph into, use this command:

    python xplor.py name name_of_your_choice

    have fun :)

    """)

else:
   print("There was an issue with setup. Setup unsuccesful.")
