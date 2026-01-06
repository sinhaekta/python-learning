import re

text = "The rain in Spain stays mainly in the plain."
pattern = r"in"
match = re.match(pattern, text)
print(match)
# o/p: None

if match:
    print("Match found:", match.group())
else:
    print("No match found")
# o/p: No match found

pattern2 = r"The"
match2 = re.match(pattern2, text)
print(match2)
# o/p: <re.Match object; span=(0, 3), match='The'>

if match2:
    print("Match found:", match2.group())
else:
    print("No match found") 
# o/p: Match found: The