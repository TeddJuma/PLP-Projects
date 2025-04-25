import os

def modify_and_copy_file():
    filename = input("Enter the name of the file to read from (e.g., sample.txt): ")
    current_dir = os.getcwd()
    full_path = os.path.join(current_dir, filename)

    try:
        # Try to open the file for reading using full path
        with open(full_path, "r") as infile:
            lines = infile.readlines()

        # Modify the content: reverse each line
        modified_lines = [line[::-1] for line in lines]

        # Write to a new file in the same directory
        new_filename = "modified_" + filename
        output_path = os.path.join(current_dir, new_filename)

        with open(output_path, "w") as outfile:
            outfile.writelines(modified_lines)

        print(f"✅ Success: Modified file saved as '{output_path}'")

    except FileNotFoundError:
        print(full_path)
        print(f"❌ Error: File '{filename}' not found in directory: {current_dir}")
    except IOError:
        print(f"❌ Error: Could not read from '{full_path}'.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
modify_and_copy_file()
