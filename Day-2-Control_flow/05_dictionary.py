server = {"name": "server1", "ip": "192.168.1.1", "status": "active"}

# Accessing dictionary values
print("Server Name:", server["name"])
print("Server IP:", server["ip"])

# Adding a new key-value pair
server["location"] = "Data Center 1"
print("Updated Server Dictionary:", server)

# Looping through dictionary keys and values
for key, value in server.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
if "status" in server:
    print("Status key found in the server dictionary.")
else:
    print("Status key not found in the server dictionary.")

# Removing a key-value pair
del server["status"]
print("Server Dictionary after removing status:", server)   