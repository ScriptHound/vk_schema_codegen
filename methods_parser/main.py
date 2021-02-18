import logging
import json
from utils.os_utils import create_results_dir
from utils.titles import Imports
from .models import ClassForm

logging.basicConfig(level=logging.INFO)

default_imports = {
    "typing": ("Optional", "Any", "List"),
    ".base_category": ("BaseCategory",)
}

def parse_file(filepath: str, imports: dict = {}) -> None:
    default_imports.update(imports)
    base_dir = create_results_dir('results/methods')
    categories = sort_json_schema(filepath)

    for category, methods in categories.items():
        with open(f"{base_dir}/{category}.py", 'w') as pyfile:
            write_done_schema(pyfile, category, methods)
    logging.info("DONE")

def write_done_schema(file, category, methods):
    file.write("from vkbottle_types.responses import %s, base\n" % category)
    file.write(str(Imports(default_imports)))
    form = ClassForm(category)
    for method in methods:
        form.add_method(method['name'], method)
    file.write(str(form))

def sort_json_schema(path: str) -> dict:
    with open(path, 'r') as f:
        json_dict = json.load(f)
    return collecter(json_dict['methods'])

def collecter(methods: dict) -> dict:
    result = {}
    for method in methods:
        method_name = method['name'].split('.')
        if result.get(method_name[0]):
            result[method_name[0]].append(method)
        else:
            result[method_name[0]] = [method]
    return result