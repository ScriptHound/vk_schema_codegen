from config import yaml_processing
import json
import re
import logging
from models.schema_objects import schema_object_fabric_method
logging.basicConfig(level=logging.INFO)

CONFIG = yaml_processing.get_config('config/config.yaml')
objects_path: str = CONFIG['schema_objects_path']


def get_json_dict(path: str) -> dict:
    with open(path, 'r') as f:
        return json.loads(f.read())


def snake_case_to_camel_case(string_list: list) -> list:
    words_list: list = []
    pattern: re.Pattern = re.compile(r'\w*?(_.)')
    for word in string_list:
        chars = re.findall(pattern, word)
        for ch in chars:
            word = word.replace(ch, ch[-1].upper())
        word = word.replace(word[0], word[0].upper())

        words_list.append(word)
    return dict(zip(string_list, words_list))


def shift_json_dict_names(plain_data: str, classnames: str) -> None:
    prepared_dict: dict = {}
    for k, v in classnames.items():
        prepared_dict[v] = plain_data[k]
    return prepared_dict


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
