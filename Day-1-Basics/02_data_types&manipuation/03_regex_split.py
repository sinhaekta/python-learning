import re
text = "The rain in Spain stays mainly in the plain."
pattern = r"in"

splits = re.split(pattern, text)
print(splits)
# o/p: ['The ra', ' ', ' Spa', ' stays ma', 'ly ', ' the pla', '.']