# backend/config/settings/dev.py
import os
from pathlib import Path

from dotenv import load_dotenv

from .base import *

# 1. Navigate up 3 levels to reach the true root folder (crm/)
# Current file: backend/config/settings/base.py
# .parent -> settings/
# .parent.parent -> config/
# .parent.parent.parent -> backend/
# .parent.parent.parent.parent -> crm/ (Root containing .env)
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent

# 2. Explicitly point to the .env file in the root
ENV_PATH = ROOT_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

DEBUG = os.environ.get("DJANGO_DEBUG", "False").lower() in ("true", "1", "t")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")

CELERY_TASK_ALWAYS_EAGER = False
