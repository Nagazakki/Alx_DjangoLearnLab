from .settings import *
import os
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["Nagazakki.onrender.com"]

SECRET_KEY = os.environ.get("@Holaputa5")

CSRF_TRUSTED_ORIGINS = ["https://Nagazakki.onrender.com"]

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL')
    )
}

# Static files (use Whitenoise for serving)
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Security settings
SECURE_BROWSER_XSS_FILTER = True
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True  # if you have HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Allowed origins for frontend/API clients
CORS_ALLOWED_ORIGINS = [
    'https://your-frontend.com',
]

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'social_media_api.settings.dev')

# Logging (optional but useful)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO',
    },
}

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


