import os
print("🔍 Looking in:", os.getcwd())


with open("text.txt", "r") as infile:
            lines = infile.readlines()
            print (lines)
            
        