import hashlib as h
import json
from pathlib import Path

config_path = Path(__file__).parent / "config/config.json"

with open(config_path, "r", encoding="utf-8") as f:
    config = json.load(f)

dummy = {
    "id": "potato",
    "password": "arbitrary_password",
    "auth": "<master>",
    "email": "user@example.com"
}

def saltHash(data: dict, salt: str) -> str:
    # Combine the data with the salt
    combined = json.dumps(data, sort_keys=True) + salt
    # Hash the combined string
    return h.sha256(combined.encode()).hexdigest()

def main():
    default_salt = "potato"
    load_config = config.get("config", {})

    if load_config is None:
        print("No config found.")
        raise ValueError("Config not found in JSON.")

    salt = load_config.get("salt", default_salt)

    print(f"Using salt: {salt}")

    hashed_data = saltHash(dummy, salt)
    print(f"Hashed data: {hashed_data}")

if __name__ == "__main__":
    main()