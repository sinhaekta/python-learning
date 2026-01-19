# String manipulation in Python

# 1. Concatenation
str1 = "Hello"
str2 = "World"
greeting = str1 + " " + str2
print(greeting)  # Output: Hello World  

# 2. Slicing
sample_str = "PythonProgramming"
print(sample_str[0:6])  # Output: Python
print(sample_str[6:])   # Output: Programming
print(sample_str[:6])   # Output: Python    

# 3. String Methods
text = "  Data Science with Python  "
print(text.lower())        # Output:   data science with python
print(text.upper())        # Output:   DATA SCIENCE WITH PYTHON
print(text.strip())       # Output: Data Science with Python
print(text.replace("Python", "R"))  # Output:   Data Science with R
print(text.split())       # Output: ['Data', 'Science', 'with', 'Python']   

# 4. Formatting
name = "Alice"
age = 30
intro = "My name is {} and I am {} years old.".format(name, age)
print(intro)  # Output: My name is Alice and I am 30 years old.

# 5. f-Strings (Python 3.6+)
intro_f = f"My name is {name} and I am {age} years old."
print(intro_f)  # Output: My name is Alice and I am 30 years old.

# 6. Finding Substrings
sentence = "Data analysis is fun"
print(sentence.find("analysis"))  # Output: 5
print(sentence.index("fun"))      # Output: 16  

# 7. Checking Membership
print("Data" in sentence)   # Output: True
print("Python" not in sentence)  # Output: True

# 8. Escape Characters
escaped_str = "He said, \"Python is awesome!\"\nLet's learn it."
print(escaped_str)
# Output:
# He said, "Python is awesome!"
# Let's learn it.   

# 9. Multiline Strings
multiline_str = """This is a multiline string.
It can span multiple lines.
Useful for documentation."""
print(multiline_str)
# Output:
# This is a multiline string.
# It can span multiple lines.
# Useful for documentation. 

# 10. String Length
print(len(sample_str))  # Output: 17    

# 11. Iterating through a String
for char in "Data":
    print(char)
# Output:
# D
# a
# t
# a 

# 12. Reversing a String
original = "Hello"
reversed_str = ""
for char in original:
    reversed_str = char + reversed_str
print(reversed_str)  # Output: olleH

# 13. Joining Strings
words = ["Data", "Science", "is", "fun"]
joined_str = " ".join(words)
print(joined_str)  # Output: Data Science is fun

# 14. String Comparison
str_a = "apple"
str_b = "banana"
print(str_a == str_b)  # Output: False
print(str_a < str_b)   # Output: True (lexicographical comparison)  

# 15. String Conversion
num = 100
num_str = str(num)
print(num_str)         # Output: '100'
print(type(num_str))   # Output: <class 'str'>
float_str = "12.34"
num_float = float(float_str)
print(num_float)       # Output: 12.34
print(type(num_float)) # Output: <class 'float'>    

# 16. Raw Strings
raw_str = r"C:\Users\Name\Documents"
print(raw_str)  # Output: C:\Users\Name\Documents

# 17. String Encoding and Decoding
original_str = "Data Science"
encoded_str = original_str.encode("utf-8")
print(encoded_str)  # Output: b'Data Science'   
decoded_str = encoded_str.decode("utf-8")
print(decoded_str)  # Output: Data Science

# 18. Checking String Properties
check_str = "Data123"
print(check_str.isalpha())  # Output: False
print(check_str.isdigit())  # Output: False
print(check_str.isalnum())  # Output: True
print("   ".isspace())      # Output: True  