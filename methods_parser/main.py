import logging
import json
from utils.os_utils import create_results_dir

logging.basicConfig(level=logging.INFO)


def parse_file(filepath: str) -> None:
    files_dir = create_parsed_files_dir('results/methods')
    filenames = set()

    with open(filepath, 'r') as f:
        json_dict = json.load(f)
        filenames = categorize_methods_as_files(json_dict, files_dir)

    for filename in filenames:
        with open(files_dir + "/" + filename + '.py', 'w'):
            pass


def create_parsed_files_dir(dir_name: str) -> None:
    create_results_dir(dir_name)
    return dir_name


def categorize_methods_as_files(json_dict: dict, files_dir: str) -> set:
    filenames = set()
    for method_dict in json_dict['methods']:
        method_name = method_dict['name'].split('.')[0]
        filenames.add(method_name)
    return filenames
