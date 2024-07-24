#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from config import Config
from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger()


def create_app(config=Config):
    template = { 
            "info": {
                "title": "My Flask API",
                "description": "An example API using Flask and Swagger",
                "version": "1.0.0"
        }
    }
    swagger.template = template
    app.init(swagger)
    return app 