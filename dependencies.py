#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Some health care"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from typing import Annotated

from fastapi import Header, HTTPException


# async def get_token_header(x_token: Annotated[str, Header()]):
#    if x_token != "fake-super-secret-token":
#        raise HTTPException(status_code=400, detail="X-Token header invalid")
#
#
# async def get_query_token(token: str):
#    if token != "jessica":
#        raise HTTPException(status_code=400, detail="No Jessica token provided")
