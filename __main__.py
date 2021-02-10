import objects_parser.main
import methods_parser.main
import responses_parser.main
from config import yaml_processing
import pytest

pytest.main()

CONFIG = yaml_processing.get_config('config/config.yaml')
objects_path: str = CONFIG['schema_objects_path']
methods_path: str = CONFIG['schema_methods_path']
responses_path: str = CONFIG['schema_responses_path']

objects_imports: dict = CONFIG['object_models_imports']

if __name__ == "__main__":
    objects_parser.main.parse_file(objects_path, objects_imports)
    methods_parser.main.parse_file(methods_path)
    responses_parser.main.parse_file(responses_path)
