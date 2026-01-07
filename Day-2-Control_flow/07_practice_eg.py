servers = [
    {"name": "server1", "status": "active"},
    {"name": "server2", "status": "inactive"},
    {"name": "server3", "status": "active"}
]

for server in servers:
    if server["status"] == "inactive":
        print(f"{server['name']} is inactive, skipping...")
    else:
        print(f"Performing maintenance on {server['name']}...")
        