import os
from pathlib import Path

from app.settings.paths import TMP_IMAGE_PATH


def get_names_from_directory(directory):
    return [Path(directory, f).as_posix() for f in os.listdir(directory)]


def file_cleanup(func):
    def decorated_function(*args, **kwargs):
        result = func(*args, **kwargs)
        file__to_remove_path = Path(TMP_IMAGE_PATH, kwargs['user_id'])
        os.remove(file__to_remove_path)
        return result
    return decorated_function
