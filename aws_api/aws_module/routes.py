#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from flask import Blueprint
from flask_cors import cross_origin
from common.constants import HTTPMethods

aws = Blueprint("aws", __name__)


@cross_origin()
@aws.route("/api", methods=[HTTPMethods.GET])
def aws_query():
    return {"message": "Data found from big query"}
