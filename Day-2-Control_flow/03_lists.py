containers = ["nginx", "mysql", "redis"]

containers.append("postgresql")
print("Containers after append:", containers)

containers.remove("mysql")
print("Containers after remove:", containers)

print(containers[0]) # Accessing first element

#Looping through the list
for container in containers:
    print("Container:", container)