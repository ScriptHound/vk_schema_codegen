import yaml
from pathlib import Path


def get_config(filepath):
    filepath: Path = Path('.') / filepath
    with open(filepath.absolute(), 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.Loader)
        return data
