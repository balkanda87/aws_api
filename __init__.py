#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Some health care"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from fastapi import FastAPI


def create_app():
    """
    function create_app create fast api object
    Returns:
        FastAPI: Fast api app object
    """
    return FastAPI()
