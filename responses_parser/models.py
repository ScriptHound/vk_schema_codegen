class ResponseModelBody:
    def __init__(self, **attributes) -> None:
        self.attributes = attributes

    def __repr__(self):
        return '\n\t'.join([f'{name} = {value}'
                           for name, value in self.attributes.items()])


class ResponseModel:
    def __init__(self,
                 classname: str,
                 superclass="BaseResponse",
                 **variables):
        self.variables = variables
        self.classname = classname
        self.superclass = superclass

    def __repr__(self):
        header = f'\n\n\nclass {self.classname}({self.superclass}):\n\t'
        body = str(ResponseModelBody(**self.variables))
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
        # HARDCODED SEEMS LIKE THIS IS UNIQUE CASE
        if json_properties['response'].get('patternProperties'):
            return SingleTypeModel(classname, 'typing.Dict[str, int]')

        properties = json_properties['response']['properties']
        properties = {name: None for name in properties.keys()}
        json_properties = {name: None for name in properties}
        return ResponseModel(classname, **json_properties)
