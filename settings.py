# secure

CSRF_COOKIE_SECURE = True   # Protection MITM attack
SESSION_COOKIE_SECURE = True  # Protection MITM attack
SECURE_BROWSE_XSS_FILTER = True  # Protection XSS attack
SECURE_CONTENT_TYPE_NOSNIFF = True  # Protection XSS attack
SECURE_SSL_REDIRECT = True # Redirect to SSL
SECURE_HOST_SECONDS = 86400  # Increasing the security of the transport layer
SECURE_HOST_INCLUDE_SUBDOMAINS = True  # Increasing the security of the transport layer
SECURE_HOST_PRELOAD = True  # Increasing the security of the transport layer