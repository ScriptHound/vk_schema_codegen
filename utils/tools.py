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


def create_objects_from_enum_types(definitions: dict):
    sorted_dict = {}
    for key, value in definitions.items():
        properties = value.get("properties")
        if not properties:
            sorted_dict[key] = value
            continue
        for item_name, item_value in properties.items():
            item_type = item_value.get("type")
            item_enum = item_value.get("enum")
            item_description = item_value.get("description")
            if not (item_type and item_enum):
                continue
            enum_name = (
                (key + "_" + item_name) if item_name in sorted_dict else item_name
            )
            sorted_dict[enum_name] = item_value
            properties[item_name] = {"$ref": f"objects.json#/definitions/{enum_name}"}
            if item_description:
                properties[item_name]["description"] = item_description
        sorted_dict[key] = value
    return sorted_dict


def get_response_imports(definitions: dict):
    imports = []
    for value in definitions.values():
        properties = value.get("properties", {})
        response = properties.get("response", {})
        ref = response.get("$ref")
        if ref:
            imports.append(get_type_from_reference(ref))
            continue
        if response.get("PatternProperties"):
            continue
        for item in [*response.get("properties", {}).values(), response]:
            if item.get("type") == "array":
                ref = item["items"].get("$ref")
            else:
                ref = item.get("$ref")
            if ref:
                imports.append(get_type_from_reference(ref))
    return {"vkbottle_types.objects": sorted(set(imports))}
