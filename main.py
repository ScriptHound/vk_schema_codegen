from config import yaml_processing
import json
import re
import logging
from models.models import ClassForm
logging.basicConfig(level=logging.INFO)

CONFIG = yaml_processing.get_config('config/config.yaml')
objects_path: str = CONFIG['schema_objects_path']


def get_dict(path: str) -> dict:
    with open(path, 'r') as f:
        return json.loads(f.read())


def camel_case_strings(string_list: list) -> list:
    words_list: list = []
    pattern: re.Pattern = re.compile(r'\w*?(_.)')
    for word in string_list:
        chars = re.findall(pattern, word)
        for ch in chars:
            word = word.replace(ch, ch[-1].upper())
        word = word.replace(word[0], word[0].upper())

        words_list.append(word)
    return dict(zip(string_list, words_list))


def prepare_data(plain_data: str, classnames: str) -> None:
    prepared_dict: dict = {}
    for k, v in classnames.items():
        prepared_dict[v] = plain_data[k]
    return prepared_dict


def handle_classes(prepared_dict: dict) -> None:
    with open('codegen.py', 'a') as pyfile:
        for classname in prepared_dict.keys():
            class_form: ClassForm = ClassForm(classname)
            try:
                for name in prepared_dict[classname]['properties'].keys():
                    text = prepared_dict[classname]['properties'][name]['description']
                    class_form.add_param(name, None)
                    class_form.add_description_row(name, text)
                pyfile.write(str(class_form))
            except KeyError:
                continue


def parse_file(path: str) -> None:
    types_dict: dict = get_dict(path)['definitions']
    classnames: list = camel_case_strings(types_dict.keys())
    prepared_dict: dict = prepare_data(types_dict, classnames)
    handle_classes(prepared_dict)

    logging.info("READY")


if __name__ == "__main__":
    parse_file(objects_path)
