import json
import re
from keyword import kwlist


def get_type_from_reference(str_ref, convert_to_calmel_case=True) -> str:
    pattern = r".*/(.*)"
    ref_type = re.search(pattern, str_ref).group(1)
    if convert_to_calmel_case:
        return snake_case_to_camel_case(ref_type)
    return ref_type


def get_annotation_type(item: dict):
    if item.get("type") == "array":
        if item["items"].get("type"):
            type_anno = [item["items"]["type"]]
        else:
            type_anno = item["items"].get("$ref")
            type_anno = [get_type_from_reference(type_anno)]
    elif item.get("type") and not item.get("$ref"):
        type_anno = item.get("type")
    elif item.get("oneOf"):
        type_anno = [get_annotation_type(item) for item in item["oneOf"]]
    else:
        type_anno = item.get("$ref")
        type_anno = get_type_from_reference(type_anno)
    return type_anno


def output_switch_decorator(function):
    """If input is dict, then return dict
    If input is a single element, return single element
    """

    def wrapper(arg):
        keys_type = type(dict().keys())
        if not isinstance(arg, (keys_type, list)):
            arg = {arg: arg}
        result = function(arg)
        if len(arg) == 1:
            # get first value in returned dict
            return result[next(iter(result))]
        return result

    return wrapper


def get_json_dict(path: str) -> dict:
    with open(path, "r") as f:
        return json.loads(f.read())


@output_switch_decorator
def snake_case_to_camel_case(string_list: list) -> dict:
    words_list: list = []
    for item in string_list:
        words_list.append(
            "".join(word[0].upper() + word[1:] for word in item.split("_"))
        )
    return dict(zip(string_list, words_list))


def camel_case_to_snake_case(string: str) -> dict:
    return "".join(
        "_" + symbol.lower() if symbol.isupper() else symbol for symbol in list(string)
    ).strip("_")


def convert_to_python_type(field):
    if field.lower() == "array":
        return "list"
    elif field.lower() == "boolean":
        return "bool"
    elif field.lower() == "integer":
        return "int"
    elif field.lower() == "number":
        return "float"
    elif field.lower() == "object":
        return "typing.Any"
    elif field.lower() == "string":
        return "str"
    else:
        return str(field)


def shift_json_dict_names(plain_data: str, classnames: str) -> dict:
    return {v: plain_data[k] for k, v in classnames.items()}


def categorize_methods_as_files(json_dict: dict) -> dict:
    filenames = set()
    for method_dict in json_dict["methods"]:
        method_name = method_dict["name"].split(".")[0]
        filenames.add(method_name)

    return {name: {} for name in filenames}


def resolve_property_name(name: str):
    if name[0].isdigit() or name in kwlist:
        name = "_" + name
    return name
