import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-change-this-in-production'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'LibraryProject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Custom User Model Configuration
AUTH_USER_MODEL = 'bookshelf.CustomUser'

# Media files configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# =============================================================================
# HTTPS SECURITY CONFIGURATION
# =============================================================================

# Step 1: HTTPS Enforcement Settings
# Force all HTTP requests to redirect to HTTPS
SECURE_SSL_REDIRECT = True

# Configure proxy SSL header for deployment behind reverse proxy
# Tells Django to trust the X-Forwarded-Proto header from the proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# HTTP Strict Transport Security (HSTS) configuration
# Instructs browsers to only access the site via HTTPS for 1 year (31536000 seconds)
SECURE_HSTS_SECONDS = 31536000

# Apply HSTS policy to all subdomains
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# Allow browsers to preload the HSTS policy for faster initial connections
SECURE_HSTS_PRELOAD = True

# Step 2: Secure Cookie Settings
# Ensure session cookies are only transmitted over HTTPS connections
SESSION_COOKIE_SECURE = True

# Ensure CSRF cookies are only transmitted over HTTPS connections
CSRF_COOKIE_SECURE = True

# Prevent JavaScript access to session cookies (XSS protection)
SESSION_COOKIE_HTTPONLY = True

# Prevent JavaScript access to CSRF cookies (XSS protection)
CSRF_COOKIE_HTTPONLY = True

# Step 3: Security Headers
# Prevent the site from being displayed in frames/iframes (clickjacking protection)
X_FRAME_OPTIONS = 'DENY'

# Prevent browsers from MIME-sniffing responses away from declared content-type
SECURE_CONTENT_TYPE_NOSNIFF = True

# Enable browser's built-in XSS filtering
SECURE_BROWSER_XSS_FILTER = True

# Control how much referrer information is sent with requests
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# =============================================================================
# PRODUCTION SECURITY NOTES
# =============================================================================
# 
# For production deployment:
# 1. Set DEBUG = False
# 2. Update ALLOWED_HOSTS with your domain names
# 3. Use environment variables for sensitive settings
# 4. Configure proper SSL certificates
# 5. Test all security headers using tools like:
#    - SSL Labs: https://www.ssllabs.com/ssltest/
#    - Security Headers: https://securityheaders.com/
#    - HSTS Preload: https://hstspreload.org/
# =============================================================================