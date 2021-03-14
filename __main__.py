import pytest

import methods_parser.main as meth_main
import objects_parser.main as obj_main
import responses_parser.imports_dict
import responses_parser.main as resp_main
from config import yaml_processing

pytest.main()

CONFIG = yaml_processing.get_config("config/config.yaml")
objects_path: str = CONFIG["schema_objects_path"]
methods_path: str = CONFIG["schema_methods_path"]
responses_path: str = CONFIG["schema_responses_path"]

objects_imports: dict = CONFIG["object_models_imports"]
methods_imports: dict = CONFIG["object_methods_imports"]


def generate_to_dir(dirname: str):
    responses_imports = responses_parser.imports_dict.imports

    obj_main.parse_file(objects_path, dirname, objects_imports)
    meth_main.parse_file(methods_path, dirname)
    resp_main.parse_file(responses_path, dirname, **responses_imports)
