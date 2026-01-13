# subprocess is a Python module used to run operating system commands from Python.
import subprocess

# Run a simple command
result = subprocess.run(["echo", "Hello, World!"], capture_output=True, text=True)
print("Output:", result.stdout) # result.stdout → standard output of command

# Run a command and check for errors
try:
    result = subprocess.run(["ls", "-l", "/non_existent_directory"], check=True, capture_output=True, text=True) # check=True raises CalledProcessError for non-zero exit codes
    print("Command succeeded with output:", result.stdout)
except subprocess.CalledProcessError as e:
    print("Command failed with error:", e.stderr) # e.stderr → standard error of command

# Run a command with shell=True
result = subprocess.run("echo $HOME", shell=True, capture_output=True, text=True) # $HOME is a shell variable, not a program argument.
print("Home directory is:", result.stdout.strip())      

# Commonly used functions in subprocess module
subprocess.run(
    command,
    shell=False,      # default
    capture_output=True,
    text=True,
    check=False       # raise error if True
)

