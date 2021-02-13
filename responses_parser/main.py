from .response_utils import (
    generate_response_dir,
    put_responses_by_filename
)
from .models import ResponseModel
from .models import jsonschema_object_factory


def write_response_alias(schema_body: dict, file: 'File') -> None:
    for classname, bofy in schema_body.items():
        properties = {'response': None}
        file.write(str(ResponseModel(classname, **properties)))


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

            write_response_alias(schema_body, file)

            for classname, body in schema_body.items():
                schema_object = jsonschema_object_factory(classname, body['properties'])

                # TODO .get('properties', {}).keys() is temporary
                file.write(str(schema_object))
