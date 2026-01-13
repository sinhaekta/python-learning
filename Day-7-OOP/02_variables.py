class Server:
    os_type = "Linux"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Server("web")
s2 = Server("db")

print(s1.os_type)
print(s2.os_type)

# Class variable → shared by all objects
# Instance variable → unique to each object