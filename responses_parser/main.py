from utils.titles import Imports, UpdateForwardRefs
from utils.tools import get_response_imports

from .models import jsonschema_object_factory, write_response_alias
from .response_utils import generate_response_dir, put_responses_by_filename


def parse_file(
    schema_path: str, filepath_to: str, imports: dict, tabulation="    "
) -> None:
    files_dir = f"{filepath_to}/responses"
    filenames, json_dict = generate_response_dir(schema_path, files_dir)
    categorized_responses = {name: {} for name in sorted(filenames)}
    definitions = json_dict["definitions"]

    responses_by_files = put_responses_by_filename(definitions, categorized_responses)
    return_type_annotations = {}
    for filename, schema_body in responses_by_files.items():
        with open(f"{filepath_to}/responses/{filename}.py", "w") as file:
            text = str(Imports(**imports, **get_response_imports(schema_body)))
            text_, annotations = write_response_alias(schema_body)
            text+= text_
            return_type_annotations[filename] = annotations
            for classname, body in schema_body.items():
                schema_object = jsonschema_object_factory(
                    classname + "Model", body["properties"]
                )
                if not isinstance(schema_object, list):
                    text += str(schema_object)
                    continue
                for item in schema_object:
                    text += str(item)

            text += str(UpdateForwardRefs(**schema_body, subclass="BaseResponse"))
            file.write(text.replace("\t", tabulation))
    return return_type_annotations
