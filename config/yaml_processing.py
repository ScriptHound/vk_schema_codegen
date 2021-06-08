from pathlib import Path

import yaml


def get_config(filepath):
    filepath: Path = Path(".") / filepath
    with open(filepath.absolute(), "r", encoding="utf-8") as f:
        return yaml.load(f, Loader=yaml.Loader)
