#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Health Care"
__version__ = "1.0"
__maintainer__ = "Someone"

from dataclasses import dataclass


@dataclass(frozen=True)
class HTTPMethods:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    OPTIONS = "OPTIONS"


@dataclass(frozen=True)
class HTTPClientErrorCode:
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
