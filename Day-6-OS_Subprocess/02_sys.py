#sys is a built-in Python module that gives access to system-specific parameters and functions.
# sys connects your Python script to the OS and CI/CD pipeline behavior.

import sys

try:
    with open('non_existent_file.txt', 'r') as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Error: {e}", file=sys.stderr)
    sys.exit(1)

# functions

print(sys.version)  # Get Python version
print(sys.platform)  # Get platform information
print(sys.path)  # Get module search path
print(sys.argv)  # Get command-line arguments   
sys.exit(0)  # Exit the program

# example
if len(sys.argv) != 3:
    print("Usage: python script.py <num1> <num2>", file=sys.stderr)
    sys.exit(1)

num1 = float(sys.argv[1])
num2 = float(sys.argv[2])
print(f"Sum: {num1 + num2}")