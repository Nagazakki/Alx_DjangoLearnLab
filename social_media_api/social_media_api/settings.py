from .settings.base import *

DEBUG = False
ALLOWED_HOSTS = ["*"]

SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = "DENY"
SECURE_SSL_REDIRECT = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # You can use postgres if configured
        "NAME": BASE_DIR / "db.sqlite3",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}