import re
text = "The rain in Spain stays mainly in the plain."

pattern = r"in"
searches = re.search(pattern, text)
print(searches)
# o/p: <re.Match object; span=(5, 7), match='in'>

if searches:
    print("First occurrence:", searches.group())
# o/p: First occurrence: in 
else:
    print("No match found")  