import re

text = "The rain in Spain stays mainly in the plain."
pattern = r"in"

replace = "on"

new_text = re.sub(pattern, replace, text)
print(new_text)
# o/p: The raon on Spaon stays maonly on the plaon.