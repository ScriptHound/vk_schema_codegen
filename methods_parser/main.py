import logging
import json
from utils.strings_util import categorize_methods_as_files
from utils.os_utils import create_results_dir, create_python_files

logging.basicConfig(level=logging.INFO)


def parse_file(filepath: str) -> None:
    files_dir = create_parsed_files_dir('results/methods')
    filenames = set()

    with open(filepath, 'r') as f:
        json_dict = json.load(f)
        filenames = categorize_methods_as_files(json_dict)
        create_python_files(files_dir, list(filenames.keys()))


def create_parsed_files_dir(dir_name: str) -> None:
    create_results_dir(dir_name)
    return dir_name
