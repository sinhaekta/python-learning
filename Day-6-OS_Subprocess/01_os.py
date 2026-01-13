import os

# Check if a directory exists
directory = "test_dir"
if not os.path.exists(directory):
    os.makedirs(directory)
    print(f"Directory '{directory}' created.")
else:
    print(f"Directory '{directory}' already exists.")   

# functions

os.getcwd()  # Get current working directory
os.listdir()  # List files and directories in current directory
os.remove("test_file.txt")  # Remove a file
os.rmdir("test_dir")  # Remove an empty directory
os.rename("old_name.txt", "new_name.txt")  # Rename a file or directory 
os.environ  # Access environment variables

# Execute a system command
os.system("echo Hello, World!")

# Note: Be cautious while using os.remove() and os.rmdir() as they will delete files/directories permanently.

print(os.getcwd())
print(os.listdir())

# read environment variable
print(os.environ.get("HOME"))
print(os.environ.get("PATH"))

# set environment variable
os.environ["MY_VAR"] = "my_value"
print(os.environ.get("MY_VAR"))