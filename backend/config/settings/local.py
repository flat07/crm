# backend/config/settings/local.py

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

DEBUG = True
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(",")
# CSRF_COOKIE_DOMAIN = ".lvh.me"
# SESSION_COOKIE_DOMAIN = ".lvh.me"
# CSRF_TRUSTED_ORIGINS = [
#     "http://serenity-spa.lvh.me:8000",
#     "http://*.lvh.me:8000",
# ]

INSTALLED_APPS += [
    # ...
    # "debug_toolbar",
    # "django_extensions",
    # ...
]
MIDDLEWARE += [
    # ...
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    # ...
]
INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]
SECURE_CROSS_ORIGIN_OPENER_POLICY = None
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
