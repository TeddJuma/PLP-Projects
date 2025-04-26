import os
print("🔍 Looking in:", os.getcwd(), "\n")


import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "text.txt")
with open(file_path, "r") as infile:
    lines = infile.readlines()
    for line in lines:
        print(line)
        