text = "Hello, World! Welcome to Python programming."
words = text.split()
print(words)
# o/p: ['Hello,', 'World!', 'Welcome', 'to', 'Python', 'programming.']

arn = "arn:aws:iam::123456789012:user/ektasinha"

print(arn.split())
# o/p: ['arn:aws:iam::123456789012:user/ektasinha']

print(arn.split(":"))
# o/p: ['arn', 'aws', 'iam', '', '123456789012', 'user/ektasinha']

print(arn.split(":")[5])
# o/p: user/ektasinha