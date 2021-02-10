import json
from utils.os_utils import create_results_dir, create_python_files


def get_responses_titles(json_schema) -> list:
    return [title for title in json_schema['definitions'].keys()]


def split_responses_names(json_titles: list) -> list:
    filenames = set()
    for title in json_titles:
        filenames.add(title.split("_")[0])
    return list(filenames)


def parse_file(schmema_path: str, **imports) -> None:
    files_dir = 'results/responses'
    create_results_dir(files_dir)

    with open(schmema_path, 'r') as schema:
        json_dict = json.load(schema)
        titles = get_responses_titles(json_dict)
        filenames = split_responses_names(titles)
        create_python_files(files_dir, filenames)
