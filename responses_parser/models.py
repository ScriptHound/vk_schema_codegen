from objects_parser.models.models import Annotation


class ResponseModelBody:
    def __init__(self, annotations=None, **attributes) -> None:
        if annotations:
            annotations = [Annotation(anno) for anno in annotations]
        else:
            annotations = ['' for _ in attributes]

        self.annotated_names = [
            name + str(annotation)
            for name, annotation in zip(attributes.keys(), annotations)
        ]
        self.attributes = {name: attributes[orig_name]
                           for name, orig_name in zip(
                                                     self.annotated_names,
                                                     attributes.keys()
                          )}

    def __repr__(self):
        return '\n\t'.join([f'{name} = {value}'
                           for name, value in self.attributes.items()])


class ResponseModel:
    def __init__(self,
                 classname: str,
                 annotations=None,
                 superclass="BaseResponse",
                 **variables):
        self.variables = variables
        self.classname = classname
        self.superclass = superclass
        self.annotations = annotations

    def __repr__(self):
        header = f'\n\n\nclass {self.classname}({self.superclass}):\n\t'
        body = str(ResponseModelBody(self.annotations, **self.variables))
        return header + body


class SingleTypeModel:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f'\n\n\n{self.name}Model = {self.value}'


def jsonschema_object_factory(classname: str, json_properties: dict) -> 'Model':
    schema_type = json_properties['response'].get('type', '$ref')

    if schema_type == '$ref':
        return SingleTypeModel(classname, None)
    elif schema_type == 'integer':
        return SingleTypeModel(classname, None)
    elif schema_type == 'boolean':
        return SingleTypeModel(classname, 'bool')
    elif schema_type == 'array':
        return SingleTypeModel(classname, 'array')
    elif schema_type == 'string':
        return SingleTypeModel(classname, 'string')
    else:
        # HARDCODED THIS IS UNIQUE CASE
        if json_properties['response'].get('patternProperties'):
            return SingleTypeModel(classname, 'typing.Dict[str, int]')

        properties = json_properties['response']['properties']
        names = {name: None for name in properties.keys()}
        json_properties = {name: None for name in names}
        types = []
        try:
            types = [value['type'] for _, value in properties.items()]
        except KeyError:
            # TODO HANDLE MISSED KEYS
            pass
        return ResponseModel(classname, types, **json_properties)
