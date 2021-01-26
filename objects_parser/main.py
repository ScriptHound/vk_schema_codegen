import logging
from os import path, mkdir, getcwd
from utils.strings_util import (
    get_json_dict,
    snake_case_to_camel_case,
    shift_json_dict_names
)
from .models.schema_objects import schema_object_fabric_method
from .models.titles import Imports, UpdateForwardRefs

logging.basicConfig(level=logging.INFO)


def create_results_dir(dir_name: str) -> None:
    try:
        mkdir(path.normpath(path.join(getcwd(), 'results')))
    except FileExistsError:
        logging.info(f'{dir_name} dir already exists')


def write_translated_json(prepared_dict: dict, imports: dict) -> None:
    create_results_dir('results')

    with open('results/codegen.py', 'a') as pyfile:
        pyfile.write(str(Imports(imports)))

        for classname in prepared_dict.keys():
            class_form = schema_object_fabric_method(classname, prepared_dict)
            pyfile.write(str(class_form))

        pyfile.write(str(UpdateForwardRefs(prepared_dict)))


def parse_file(path: str, imports_dict: dict) -> None:
    types_dict: dict = get_json_dict(path)['definitions']
    classnames: list = snake_case_to_camel_case(types_dict.keys())
    prepared_dict: dict = shift_json_dict_names(types_dict, classnames)
    write_translated_json(prepared_dict, imports_dict)

    logging.info("READY")