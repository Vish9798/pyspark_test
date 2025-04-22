import json
import os
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

def load_config(path):
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Config file '{path}' not found.")

    ext = path.suffix.lower()

    if ext == ".json":
        with open(path, "r") as f:
            return json.load(f)

    elif ext in [".yaml", ".yml"]:
        if yaml is None:
            raise ImportError("pyyaml not installed. Install it with `pip install pyyaml`")
        with open(path, "r") as f:
            return yaml.safe_load(f)

    else:
        raise ValueError("Unsupported config file format. Use .json or .yaml/.yml")

def validate_config(config):
    if "transformations" not in config:
        raise ValueError("Missing 'transformations' section in configuration.")
    if "actions" not in config:
        raise ValueError("Missing 'actions' section in configuration.")