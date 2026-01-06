server_name = input("Enter the server name:")
environment = input("Enter the environment (dev/prod):")
cpu_usage = float(input("Enter the CPU usage (%):"))

if cpu_usage > 80:
    print(f"Alert! High CPU usage on {server_name} in {environment} environment: {cpu_usage}%")
else:
    print(f"{server_name} CPU usage is normal.")