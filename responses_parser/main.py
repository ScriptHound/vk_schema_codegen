from utils.titles import Imports, UpdateForwardRefs
from utils.tools import get_response_imports
from .models import ResponseModel, jsonschema_object_factory
from .response_utils import generate_response_dir, put_responses_by_filename


def write_response_alias(schema_body: dict, file) -> None:
    for classname in schema_body.keys():
        annotation = f': Optional["{classname}Model"]'
        properties = {"response" + annotation: None}
        file.write(str(ResponseModel(classname, **properties)))


def parse_file(schema_path: str, filepath_to: str, imports) -> None:
    files_dir = f"{filepath_to}/responses"
    filenames, json_dict = generate_response_dir(schema_path, files_dir)
    categorized_responses = {name: {} for name in sorted(filenames)}
    definitions = json_dict["definitions"]

    responses_by_files = put_responses_by_filename(definitions, categorized_responses)

    for filename, schema_body in responses_by_files.items():
        with open(f"{filepath_to}/responses/{filename}.py", "w") as file:
            file.write(str(Imports(**imports, **get_response_imports(schema_body))))
            write_response_alias(schema_body, file)

            for classname, body in schema_body.items():
                schema_object = jsonschema_object_factory(
                    classname + "Model", body["properties"]
                )

                file.write(str(schema_object))
            file.write(str(UpdateForwardRefs(**schema_body, subclass="BaseResponse")))
