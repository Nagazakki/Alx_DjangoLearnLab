# Add these configurations to your Django project's settings.py file

# LOGIN/LOGOUT URLs
LOGIN_URL = '/login/'  # Where to redirect if login is required
LOGIN_REDIRECT_URL = '/'  # Where to redirect after successful login
LOGOUT_REDIRECT_URL = '/'  # Where to redirect after logout

# Message framework settings (for displaying login/logout messages)
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger',
}

# Ensure these apps are in INSTALLED_APPS (they should already be there)
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # Required for authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Required for sessions
    'django.contrib.messages',  # Required for messages
    'django.contrib.staticfiles',
    'relationship_app',  # Your app
    # ... other apps
]

# Middleware configuration (ensure these are present)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required for sessions
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required for auth
    'django.contrib.messages.middleware.MessageMiddleware',  # Required for messages
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Session settings (optional customization)
SESSION_COOKIE_AGE = 3600  # Session expires after 1 hour of inactivity
SESSION_SAVE_EVERY_REQUEST = True  # Update session on every request

# Password validation settings
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]