from objects_parser.models.models import Annotation
from utils.strings_util import convert_to_python_type, get_type_from_reference


class ResponseModelBody:
    def __init__(self, annotations=None, **attributes) -> None:
        if annotations:
            temp = []
            for anno in annotations:
                if isinstance(anno, list):
                    temp.append(Annotation("Array", list_inner_type=anno))
                else:
                    temp.append(Annotation(anno))

            annotations = temp
        else:
            annotations = ["" for _ in attributes]

        self.annotated_names = [
            name + str(annotation)
            for name, annotation in zip(attributes.keys(), annotations)
        ]

    def __repr__(self):
        return "\n\t".join(f"{name} = None" for name in self.annotated_names)


class ResponseModel:
    def __init__(
        self, classname: str, annotations=None, superclass="BaseResponse", **variables
    ):
        self.variables = variables
        self.classname = classname
        self.superclass = superclass
        self.annotations = annotations

    def __repr__(self):
        header = f"\n\nclass {self.classname}({self.superclass}):\n\t"
        body = str(ResponseModelBody(self.annotations, **self.variables))
        return header + body + "\n"


class SingleTypeModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"\n\n{self.name} = {self.value}\n".replace(": ", "")


def write_response_alias(schema_body: dict) -> None:
    text = ""
    annotations = {}
    for classname, value in schema_body.items():
        schema_type = value["properties"]["response"].get("type", "$ref")
        if schema_type == "$ref":
            annotation = convert_to_python_type(
                get_type_from_reference(value["properties"]["response"]["$ref"])
            )
        elif schema_type == "array":
            type_ = value["properties"]["response"]["items"].get("type")
            if not type_:
                type_ = value["properties"]["response"]["items"]["$ref"]
                annotation = f'typing.List["{get_type_from_reference(type_)}"]'
            elif type_ == "object":
                annotation = f'typing.List["{classname}Model"]'
            else:
                annotation = f"typing.List[{convert_to_python_type(type_)}]"
        # HARDCODED THIS IS UNIQUE CASE
        elif value["properties"]["response"].get("patternProperties"):
            annotation = "typing.Dict[str, int]"
        elif schema_type == "object":
            annotation = f'"{classname}Model"'
        else:
            annotation = convert_to_python_type(schema_type)
        annotations[classname] = annotation
        properties = {"response: " + annotation: None}
        text += str(ResponseModel(classname, **properties))
    return text, annotations


def jsonschema_object_factory(classname: str, json_properties: dict):
    schema_type = json_properties["response"].get("type", "$ref")

    if schema_type == "array":
        type_ = json_properties["response"]["items"].get("type")
        if type_ == "object":
            properties = json_properties["response"]["items"]["properties"]
            return ResponseModel(classname, get_types(properties), **properties)
        return ""
    elif schema_type in [
        "$ref",
        "integer",
        "number",
        "string",
        "boolean",
    ] or json_properties["response"].get("patternProperties"):
        return ""

    properties = json_properties["response"]["properties"]
    names = {name: None for name in properties.keys()}
    json_properties = {name: None for name in names}
    types = get_types(properties)
    return ResponseModel(classname, types, **json_properties)


def get_types(properties: dict):
    types = []
    for value in properties.values():
        property_type = value.get("type")
        if not property_type:
            t = get_type_from_reference(value["$ref"])
            types.append(t)
            continue
        elif property_type == "array":
            ref_type = value["items"].get("$ref")
            if not ref_type:
                types.append([value["items"]["type"]])
                continue
            types.append([get_type_from_reference(ref_type)])
        else:
            types.append(value["type"])
    return types
