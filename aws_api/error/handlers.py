#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from flask import Blueprint, abort
from common.constants import HTTPClientErrorCode

error = Blueprint("error", __name__)


@error.app_error_handler(HTTPClientErrorCode.BAD_REQUEST)
def bad_request(error):
    """bad_request error handler"""
    abort(
        HTTPClientErrorCode.BAD_REQUEST,
        {"message": "Bad request unable to process this request!"},
    )
