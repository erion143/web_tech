sudo gunicorn --bind 0.0.0.0:8080 --access-logfile acc.log --error-logfile err.log ask.wsgi:application
