from pathlib import Path

APP_DIR = Path(__file__).resolve().parent

with open(APP_DIR/'VERSION') as version:
    __version__ =  version.read()