web: waitress-serve --port=${PORT:-8000} src.core.wsgi:APPLICATION
worker: python src/manage.py celery worker