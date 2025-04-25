import os

# 1. Function to read from a file
def read_file(filename):
    try:
        with open(filename, "r") as infile:
            content = infile.read()
        return content
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found.")
        return None
    except IOError:
        print(f"❌ Error: Could not read from '{filename}'.")
        return None

# 2. Function to modify the content
def modify_content(content):
    # Example modification: convert to uppercase and add a footer line
    modified = content.upper()
    modified += "\n\n--- File processed successfully. ---"
    return modified

# 3. Function to write to a new file
def write_file(new_filename, content):
    try:
        with open(new_filename, "w") as outfile:
            outfile.write(content)
    except IOError:
        print(f"❌ Error: Could not write to '{new_filename}'.")

# 4. Call functions in sequence
def process_file():
    filename = input("Enter the name of the file to read (e.g., sample.txt): ")
    cwd = os.getcwd()
    full_path = os.path.join(cwd, filename)

    original_content = read_file(full_path)

    if original_content:
        modified_content = modify_content(original_content)
        new_filename = os.path.join(cwd, "modified_" + filename)
        write_file(new_filename, modified_content)

        # 5. Print success message
        print(f"✅ Success: Modified content written to '{new_filename}'")

# Run the process
process_file()
