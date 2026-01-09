# Read and filter errors

with open("app.log", "r") as log_file:
    for line in log_file:
        if "ERROR" in line:
            print(line.strip())

# Writing Logs

from datetime import datetime

def write_log(message, level="INFO"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("system.log", "a") as log_file:
        log_file.write(f"{timestamp} - {level} - {message}\n")

# Example usage
write_log("Application started")
write_log("An error occurred", level="ERROR")