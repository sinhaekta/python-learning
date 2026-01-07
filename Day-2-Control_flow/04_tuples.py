# Immutable data structures in Python

ports = (22, 80, 443, 8080)

# Accessing elements
print("First port:", ports[0])

# Looping through the tuple
for port in ports:
    print("Port:", port)

# Trying to modify a tuple (will raise an error)
try:
    ports[0] = 21
except TypeError as e:
    print("Error:", e)
# o/p: Error: 'tuple' object does not support item assignment

# Tuple unpacking
http_port, https_port, ftp_port, ssh_port = ports
print("HTTP Port:", http_port)
print("HTTPS Port:", https_port)
print("FTP Port:", ftp_port)
print("SSH Port:", ssh_port)
# o/p: HTTP Port: 22
# o/p: HTTPS Port: 80
# o/p: FTP Port: 443
# o/p: SSH Port: 8080   