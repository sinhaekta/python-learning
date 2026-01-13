# Check if config file exists
import os
import logging

logging.basicConfig(level=logging.INFO)

config_file = "config.json"

if not os.path.exists(config_file):
    logging.error("Config file missing")
    raise FileNotFoundError("config.json not found")

logging.info("Config file found")
