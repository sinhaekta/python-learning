import yaml

# Writing YAML file
data = {
    "env": "dev",
    "replicas": 3
}

with open("config.yaml", "w") as f:
    yaml.safe_dump(data, f)


# Reading YAML file
with open("config.yaml") as f:
    config = yaml.safe_load(f)

print(config["env"])