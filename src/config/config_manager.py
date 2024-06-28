import json
import os
from typing import Dict, Any

CONFIG_FILE = 'config.json'

def save_config(config: Dict[str, Any]) -> None:
    """Save the configuration to a JSON file."""
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f)

def load_config() -> Dict[str, Any]:
    """Load the configuration from a JSON file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    return {}

def update_config(key: str, value: Any) -> None:
    """Update a specific configuration key."""
    config = load_config()
    config[key] = value
    save_config(config)

def get_config(key: str, default: Any = None) -> Any:
    """Get a specific configuration value."""
    config = load_config()
    return config.get(key, default)

def reset_config() -> None:
    """Reset the configuration to default values."""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)