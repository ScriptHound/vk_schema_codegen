from os import mkdir, path, getcwd
import logging
logging.basicConfig(level=logging.INFO)


def create_results_dir(dir_name: str) -> None:
    if not path.exists(path.normpath(path.join(getcwd(), dir_name))):
        mkdir(path.normpath(path.join(getcwd(), dir_name)))
