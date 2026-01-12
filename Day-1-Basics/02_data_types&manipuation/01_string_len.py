text = "arn:aws:iam::123456789012:user/ektasinha"

print(len(text))
# o/p: 40

print((text.split("/")))
# o/p: ['arn:aws:iam::123456789012:user', 'ektasinha']

print(len(text.split("/")))
# o/p: 2

