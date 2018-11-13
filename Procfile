web: waitress-serve --port=${PORT:-8000} src.core.wsgi:APPLICATION
worker: cd src && celery -A urldownloader worker