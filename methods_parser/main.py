import logging
import json
from utils.os_utils import create_results_dir
from objects_parser.models.titles import Imports
from .models.schema import Schematik

logging.basicConfig(level=logging.INFO)


def parse_file(filepath: str, imports: dict = {}) -> None:
    imports = imports or {"typing": ("Optional", "Any", "List"), ".base_category": ("BaseCategory",)}
    base_dir = create_results_dir('results/methods')

    with open(filepath, 'r') as f:
        json_dict = json.load(f)

    sorted_categories = collecter(json_dict['methods'])

    for category, methods in sorted_categories.items():
        with open(f"{base_dir}/{category}.py", 'w') as pyfile:
            pyfile.write(
                "from vkbottle_types.responses import %s, base\n" % category
            )
            pyfile.write(str(Imports(imports)))
            pyfile.write(Schematik(methods, category).get)

    logging.info("DONE")


def collecter(json_object: dict):
    result = {}
    for method in json_object:
        method_ = method['name'].split('.')
        if result.get(method_[0]):
            result[method_[0]].append(method)
        else:
            result[method_[0]] = [method]
    return result
