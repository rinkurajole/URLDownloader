"""
Production Settings for server.
"""
import os
# import djcelery

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Email Settings
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
# Remove host and password before push to git
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# messaging queue
CELERY_BROKER_URL = os.environ.get('REDISCLOUD_URL')
CELERY_RESULT_BACKEND = os.environ.get('CLOUDAMQP_URL')
CELERY_IMPORTS = ('urldownloader.tasks')
CELERY_ACCEPT_CONTENT = ['json', 'pickle', 'msgpack']
# CELERY_TASK_SERIALIZER = 'pickle'
# CELERY_RESULT_SERIALIZER = 'pickle'
