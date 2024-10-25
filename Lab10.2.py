import os
import shutil

os.mkdir("A_NAMES", dir_fd=None)
os.mkdir("B_NAMES", dir_fd=None)

files = [f for f in os.listdir() if os.path.isfile(f)]

for file in files:
    if file.lower().startswith("a"):
        shutil.move(file, "A_NAMES")
    elif file.lower().startswith("b"):
        shutil.move(file, "B_NAMES")
