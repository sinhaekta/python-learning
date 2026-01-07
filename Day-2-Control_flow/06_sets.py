# Unique values

ips = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}

print("Initial IPs:", ips)

# Adding a new IP
ips.add("192.168.1.4")
print("After adding an IP:", ips)   

# Removing an IP
ips.remove("192.168.1.2")
print("After removing an IP:", ips)


# Sets automatically handle duplicatess
service = ["nginx", "mysql", "redis", "nginx", "mysql"]

Unique_services = set(service)
print("Unique services:", Unique_services)  