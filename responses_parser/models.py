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
        return "\n\t".join(
            [f"{name} = None" for name in self.annotated_names]
        )


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


def jsonschema_object_factory(classname: str, json_properties: dict):
    schema_type = json_properties["response"].get("type", "$ref")

    if schema_type == "$ref":
        t = convert_to_python_type(
            get_type_from_reference(json_properties["response"]["$ref"])
        )
        return SingleTypeModel(classname, t)
    elif schema_type == "integer":
        return SingleTypeModel(classname, "int")
    elif schema_type == "boolean":
        return SingleTypeModel(classname, "bool")
    elif schema_type == "array":
        type_ = None
        if json_properties["response"]["items"].get("type"):
            type_ = json_properties["response"]["items"]["type"]
            if type_ == "object":
                properties = json_properties["response"]["items"]["properties"]
                return [
                    ResponseModel(
                        classname + "Object", get_types(properties), **properties
                    ),
                    SingleTypeModel(classname, f'typing.List["{classname + "Object"}"]'),
                ]
            type_ = Annotation("Array", list_inner_type=type_, required=True)
            return SingleTypeModel(classname, type_)
        type_ = json_properties["response"]["items"]["$ref"]
        type_ = get_type_from_reference(type_)
        return SingleTypeModel(classname, f"typing.List[{type_}]")

    elif schema_type == "string":
        return SingleTypeModel(classname, "str")
    else:
        # HARDCODED THIS IS UNIQUE CASE
        if json_properties["response"].get("patternProperties"):
            return SingleTypeModel(classname, "typing.Dict[str, int]")

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
