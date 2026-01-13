# for -> used for iterating over a sequence (like a list, tuple, dictionary, set, or string)

servers = ["server1", "server2", "server3"]

for server in servers:
    print(f"Checking status of {server}...")

# while -> repeatedly executes a block of code as long as a condition is true

retries = 0

while retries < 3:
    print(f"Attempt {retries + 1} to connect to server...")
    retries += 1



# example
services = ["nginx", "mysql", "redis"]
for service in services:
    if service == "nginx":
        print("Nginx service found, skipping...")
        continue  # Skip the rest of the loop for this iteration
    print(f"Starting service: {service}")

# for with enumerate()
function = [1, 2, 3, 4, 50]
for i,f in enumerate(function):
    print(i,f)