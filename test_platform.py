import sys

if sys.platform.startswith('win'):
    print("Running on Windows")
    print(sys.platform)
else:
    print("Not running on Windows")
