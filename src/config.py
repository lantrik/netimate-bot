from os import getenv
from pathlib import Path

### ENVIRONMENT

TOKEN = getenv("TOKEN")

MONGO_TOKEN = getenv("MONGO_TOKEN")
MONGO_NAME = getenv("MONGO_NAME")

DEVELOPER_ID = int(getenv("DEVELOPER_ID", 0))

### HANDLERS

HANDLERS_ROOT = "src"
HANDLERS = ["handlers"]

### DIRECTORIES

BASE_DIR = Path(__file__).parent.parent
PUBLIC_DIR = BASE_DIR / 'public'