from os import mkdir, path, getcwd
import logging
logging.basicConfig(level=logging.INFO)


def create_results_dir(dir_name: str) -> None:
    try:
        mkdir(path.normpath(path.join(getcwd(), dir_name)))
    except FileExistsError:
        logging.info(f'{dir_name} dir already exists')
