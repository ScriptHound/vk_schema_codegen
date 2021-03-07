import yaml
from pathlib import Path


def get_config(filepath):
    filepath = Path('.') / filepath
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.Loader)
        return data
