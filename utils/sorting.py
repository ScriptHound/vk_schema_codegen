from utils.strings_util import get_type_from_reference


def get_references(item: dict):
    references = []
    all_of = item.get("allOf", [])
    one_of = item.get("oneOf", [])
    for i in [*all_of, *one_of, item]:
        reference = i.get("$ref")
        if reference:
            references.append(get_type_from_reference(reference, False))
    return references


def sort_by_reference(definitions: dict):
    sorted_dict = {}
    for key, value in definitions.items():
        references = get_references(value)
        while references:
            reference = references[0]
            new_references = get_references(definitions[reference])
            if not new_references:
                if reference not in sorted_dict:
                    sorted_dict[reference] = definitions[reference]
                references.remove(reference)
                continue
            for ref in new_references:
                if ref in sorted_dict:
                    sorted_dict[reference] = definitions[reference]
                    if reference in references:
                        references.remove(reference)
                    continue
                references.insert(0, ref)
        if key not in sorted_dict:
            sorted_dict[key] = value
    return sorted_dict
