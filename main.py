from objects_parser.main import parse_file
from config import yaml_processing

CONFIG = yaml_processing.get_config('config/config.yaml')
objects_path: str = CONFIG['schema_objects_path']

if __name__ == "__main__":
    imports = {
        "enum": None,
        "typing": ["Any", "List", "Optional", "Union"],
        "pydantic": ["BaseModel"]
    }
    parse_file(objects_path, imports)
