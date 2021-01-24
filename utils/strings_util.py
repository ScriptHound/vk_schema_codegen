import json
import re


def get_type_from_reference(str_ref):
    pattern = re.compile('.*/(.*)')
    ref_type = re.search(pattern, str_ref).group(1)
    return snake_case_to_camel_case(ref_type)


def output_switch_decorator(function):
    def wrapper(arg):
        keys_type = type(dict().keys())
        if type(arg) != keys_type and type(arg) != list:
            arg = {arg: arg}
        result = function(arg)
        if len(arg) == 1:
            # get first value in returned dict
            return result[next(iter(result))]
        return result
    return wrapper


def get_json_dict(path: str) -> dict:
    with open(path, 'r') as f:
        return json.loads(f.read())


@output_switch_decorator
def snake_case_to_camel_case(string_list: list) -> list:
    words_list: list = []
    pattern: re.Pattern = re.compile(r'(_.)')
    for word in string_list:
        chars = re.findall(pattern, word)
        for ch in chars:
            word = word.replace(ch, ch[-1].upper())
        word = word.replace(word[0], word[0].upper(), 1)

        words_list.append(word)
    return dict(zip(string_list, words_list))


def shift_json_dict_names(plain_data: str, classnames: str) -> None:
    prepared_dict: dict = {}
    for k, v in classnames.items():
        prepared_dict[v] = plain_data[k]
    return prepared_dict
