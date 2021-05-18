import logging

from utils.os_utils import create_results_dir
from utils.strings_util import (
    get_json_dict,
    shift_json_dict_names,
    snake_case_to_camel_case,
)
from utils.titles import Imports, UpdateForwardRefs
from utils.tools import create_objects_from_enum_types, sort_by_reference

from .models.schema_objects import schema_object_fabric_method

logging.basicConfig(level=logging.INFO)


def write_translated_json(filepath_to: str, prepared_dict: dict, imports: dict) -> None:
    create_results_dir(filepath_to)

    with open(f"{filepath_to}/objects.py", "w") as pyfile:
        pyfile.write(str(Imports(**imports)))

        for classname in prepared_dict.keys():
            class_form = schema_object_fabric_method(classname, prepared_dict)
            pyfile.write(str(class_form))

        pyfile.write(str(UpdateForwardRefs(**prepared_dict)))


def parse_file(path: str, filepath_to: str, imports_dict: dict) -> None:
    types_dict: dict = create_objects_from_enum_types(
        sort_by_reference(get_json_dict(path)["definitions"])
    )
    classnames: dict = snake_case_to_camel_case(types_dict.keys())
    prepared_dict: dict = shift_json_dict_names(types_dict, classnames)
    write_translated_json(filepath_to, prepared_dict, imports_dict)

    logging.info("READY")
