containers = ["nginx", "mysql", "redis"]

containers.append("postgresql")
print("Containers after append:", containers)

containers.remove("mysql")
print("Containers after remove:", containers)

print(containers[0]) # Accessing first element

#Looping through the list
for container in containers:
    print("Container:", container)

# return ''.join(reversed(result))
# reversed(result) does NOT return a string. It returns a reverse iterator.