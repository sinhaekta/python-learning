# OOP helps in organizing code into reusable and modular components.

class Server:
    def __init__(self, name, ip_address): #Constructor
        self.name = name
        self.ip_address = ip_address
        self.status = "offline"

    def start(self):  # instance method
        self.status = "online"
        print(f"{self.name} started.")

    def stop(self):
        self.status = "offline"
        print(f"{self.name} stopped.")

    def get_status(self):
        return f"{self.name} is currently {self.status}."

s1 = Server("Server1", "192.168.1.100") # Creating an object of the Server class
# Calling method
s1.start()  
print(s1.get_status())  
s1.stop()  
print(s1.get_status())   
# Accessing attribute 
print(s1.name)  
print(s1.ip_address)  