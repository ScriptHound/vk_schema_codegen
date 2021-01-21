from config import yaml_processing
from utils.strings_util import (
    get_json_dict,
    snake_case_to_camel_case,
    shift_json_dict_names
)
import logging
from models.schema_objects import schema_object_fabric_method
logging.basicConfig(level=logging.INFO)

CONFIG = yaml_processing.get_config('config/config.yaml')
objects_path: str = CONFIG['schema_objects_path']


def write_translated_json(prepared_dict: dict) -> None:
    with open('codegen.py', 'a') as pyfile:
        for classname in prepared_dict.keys():
            class_form = None
            class_form = schema_object_fabric_method(classname, prepared_dict)
            pyfile.write(str(class_form))


def parse_file(path: str) -> None:
    types_dict: dict = get_json_dict(path)['definitions']
    classnames: list = snake_case_to_camel_case(types_dict.keys())
    prepared_dict: dict = shift_json_dict_names(types_dict, classnames)
    write_translated_json(prepared_dict)

    logging.info("READY")


if __name__ == "__main__":
    parse_file(objects_path)
