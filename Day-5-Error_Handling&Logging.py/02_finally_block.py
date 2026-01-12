try:
    f = open("data.txt")
    content = f.read()
except FileNotFoundError:
    print("File not found")
else:
    print("File read successfully")
finally: # This block will always execute regardless of exception
    print("Execution completed")


# Raise custom exception

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    else:
        print("Age is valid")