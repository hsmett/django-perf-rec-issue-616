import os

from .settings import *

INSTALLED_APPS.append("issue616")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": os.environ.get("DATABASE_PORT", ""),
        "OPTIONS": {},
    },
}

PERF_REC = {
    # https://github.com/adamchainz/django-perf-rec?tab=readme-ov-file#hide_columns
    "HIDE_COLUMNS": False,
    # https://github.com/adamchainz/django-perf-rec?tab=readme-ov-file#mode
    "MODE": "once",
}
