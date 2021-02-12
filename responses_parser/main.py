from .response_utils import (
    generate_response_dir,
    put_responses_by_filename
)


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
        header = f'\n\nclass {self.classname}({self.superclass}):\n\t'
        body = str(ResponseModelBody(**self.variables))
        return header + body


def parse_file(schema_path: str, **imports) -> None:
    files_dir = 'results/responses'
    filenames, json_dict = generate_response_dir(schema_path, files_dir)
    categorized_responses = {name: {} for name in sorted(filenames)}
    definitions = json_dict['definitions']

    responses_by_files = put_responses_by_filename(
                                                  definitions,
                                                  categorized_responses)

    for filename, schema_body in responses_by_files.items():
        with open(f'results/responses/{filename}.py', 'w') as file:
            for classname, body in schema_body.items():
                response = body['properties']['response']
                # TODO .get('properties', {}).keys() is temporary
                properties = {name: None for name in response.get('properties', {}).keys()}
                file.write(str(ResponseModel(classname, **properties)))
