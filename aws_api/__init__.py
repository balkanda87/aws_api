#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from .config import Config
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS()

def celery_create_app():
    pass

def create_app(config=Config):
    template = { 
            "info": {
                "title": "Flask aws sample app",
                "description": "An example API using Flask and Swagger",
                "version": "1.0.0"
        }
    }
    cors.init_app(app)
    
    from .aws_module.routes import aws
    app.register_blueprint(aws)
    
    return app 