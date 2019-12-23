from os import listdir
from pathlib import Path


def get_names_from_directory(directory):
    return [Path(directory, f).as_posix() for f in listdir(directory)]
