from .base import *

SECURE_SSL_REDIRECT = True
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS")
STATIC_ROOT = env("STATIC_ROOT")

# make sure that session auth related cookies
# are transmitted only over HTTPS
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Origins allowed to bypass CORS
CORS_ALLOWED_ORIGINS = [
    "https://example.com"
]

# DRF settings for PROD
REST_FRAMEWORK = {**REST_FRAMEWORK,
    # Only allows JSON endpoints and disables DRF's browsable API in PROD
    "DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]
}