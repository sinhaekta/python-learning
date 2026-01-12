import re

text = "The rain in Spain stays mainly in the plain."
pattern = r"in"
searches = re.findall(pattern, text)
print(searches)
# o/p: ['in', 'in', 'in', 'in', 'in']       