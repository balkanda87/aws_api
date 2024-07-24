#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from aws_api import create_app, celery_create_app

flask_app = create_app()
celery_app = celery_create_app()

if __name__ == '__main__':
    flask_app.run(host="0.0.0.0", port=8000, debug=True)

