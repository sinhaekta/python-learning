import json

# Writing JSON file
data = [{
    "env": "prod",
    "version": "1.0.1",
    "region": "ap-south-1"
}]

with open("config.json", "w") as f: #overwrite mode, cannot append
    json.dump(data, f, indent=4)

# Reading JSON file
with open("config.json") as f:
    config = json.load(f)

print(config[0]["env"])
print(config[0]["version"])

# Updating JSON file
new_data = {
    "env": "stg",
    "version": "1.0.2",
    "region": "ap-south-1"
}

with open("config.json", "r") as f:
    data = json.load(f)   # data is a list

data.append(new_data)

with open("config.json", "w") as f:
    json.dump(data, f, indent=4)