"""
Production Settings for server.
"""
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get(
    'SECRET_KEY', 'nmqz%)5ery(1esonrn%mt7nj5%_i56c*hjs57(=)p&femx^)ic')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
# Remove host and password before push to git
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'raj.rajole@gmail.com')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', 'kesqedrocscwbrwh')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
