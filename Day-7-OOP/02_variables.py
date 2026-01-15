class Server:
    os_type = "Linux"   # class variable

    def __init__(self, name):
        self.name = name   # instance variable

s1 = Server("web")
s2 = Server("db")

print(s1.os_type) #output: Linux
print(s2.os_type) #output: Linux

print(s1.name) #output: web
print(s2.name) #output: db

# Class variable → shared by all objects
# Instance variable → unique to each object