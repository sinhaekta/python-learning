text = "This is Python Programming"
substring = "is"

if substring in text:
    print(f'"{substring}" found in the text.')
    # o/p: "is" found in the text.
else:
    print(f'"{substring}" not found in the text.')


text = "Hello, World! Welcome to Python programming."
index = text.find("Python")
if index != -1:
    print(f'"Python" found at index {index}.')
    # o/p: "Python" found at index 21.
else:
    print('"Python" not found in the text.')