from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

IMAGES_DIR = Path(BASE_DIR, 'images')

TMP_IMAGE_PATH = Path(BASE_DIR, 'tmp')
TMP_IMAGE_PATH.mkdir(parents=True, exist_ok=True)
