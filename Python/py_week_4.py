import os

script_dir = os.path.dirname(__file__)

def read_file(filename):
    file_path = os.path.join(script_dir, filename)
    try:
        with open(file_path, "r") as file:
            content = file.read()
            print(f"✅ Success: Read content from '{filename}'\n")
        return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except IOError:
        print(f"❌ Error: Could not read from '{filename}'.")
        return None

def write_file(new_filename, content):
    new_file_path = os.path.join(script_dir, new_filename)
    try:
        with open(new_file_path, "w") as outfile:
            outfile.write(content)
    except IOError:
        print(f"❌ Error: Could not write to '{new_filename}'.")
        
def copy_content():
    filename = input("Enter the name of the file to copy (e.g., sample.txt): ")
    original_content = read_file(filename)
    
    if original_content:
        modified_content = read_file(filename)
        new_filename = "copy_" + filename
        write_file(new_filename, modified_content)

        print(f"✅ Success: {filename} content copied to '{new_filename}'")

def process_file():
    filename = input("Enter the name of the file to read (e.g., sample.txt): ")
    original_content = read_file(filename)
    print(original_content, end="\n\n*****END OF FILE*****")