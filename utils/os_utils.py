from os import DirEntry, mkdir
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)


def create_results_dir(dir_name: str) -> str:
    if not Path(dir_name).exists():
        mkdir(str(Path(dir_name)))
    return dir_name
