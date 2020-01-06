import os
from pathlib import Path


def get_names_from_directory(directory):
    return [Path(directory, f).as_posix() for f in os.listdir(directory)]
