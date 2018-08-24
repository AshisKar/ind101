web: gunicorn config.wsgi:application
worker: celery worker --app=ind101.taskapp --loglevel=info
