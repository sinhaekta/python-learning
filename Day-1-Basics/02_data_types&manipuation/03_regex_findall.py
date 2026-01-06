import re

text = "The rain in Spain stays mainly in the plain."
pattern = r"in"
searches = re.findall(pattern, text)
print(searches)
# o/p: ['in', 'in', 'in', 'in', 'in']

pattern2 = r"in"
searches2 = re.search(pattern2, text)
print(searches2)
# o/p: <re.Match object; span=(5, 7), match='in'>
if searches2:
    print("First occurrence:", searches2.group())
# o/p: First occurrence: in 
else:
    print("No match found")         

