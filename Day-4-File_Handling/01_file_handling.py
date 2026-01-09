# Reading a file
with open('example.txt', 'r') as file:
    content = file.read()
    print("File Content:")
    print(content)

# Writing to a file 
with open('output.txt', 'w') as file:
    file.write("This is a sample output file.\n")
    file.write("File handling in Python is easy!")  

# Appending to a file
with open('output.txt', 'a') as file:
    file.write("\nAppending a new line to the file.")