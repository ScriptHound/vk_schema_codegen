import json
import logging

from utils.os_utils import create_results_dir
from utils.titles import Imports
from utils.tools import get_methods_imports

from .models import ClassForm

logging.basicConfig(level=logging.INFO)


def parse_file(
    filepath: str, filepath_to: str, imports: dict, return_type_annotations: dict, tabulation="    "
) -> None:
    base_dir = create_results_dir(f"{filepath_to}/methods")
    categories = sort_jsonmethods_schema(filepath)

    for category, methods in categories.items():
        with open(f"{base_dir}/{category}.py", "w") as file:
            text = construct_schema(category, methods, imports, return_type_annotations[category]).replace(
                "\t", tabulation
            )
            file.write(text)


def construct_schema(category, methods, imports, return_type_annotations: dict):
    text = str(Imports(**imports, **get_methods_imports(methods)))
    form = ClassForm(category)
    for method in methods:
        form.add_method(method["name"], method, return_type_annotations)
    text += str(form)
    return text


def sort_jsonmethods_schema(path: str) -> dict:
    with open(path, "r") as f:
        json_dict = json.load(f)
    return collecter(json_dict["methods"])


def collecter(methods: dict) -> dict:
    result = {}
    for method in methods:
        method_name = method["name"].split(".")

        if result.get(method_name[0]):
            result[method_name[0]].append(method)
        else:
            result[method_name[0]] = [method]
    return result
