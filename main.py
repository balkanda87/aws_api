#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Some health care"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from fastapi import FastAPI
from common.constants import ApiResponse
from routers import aws

app = FastAPI()


app.include_router(aws.router)


@app.get("/")
async def root():
    return {ApiResponse.MESSAGE: "Welcome to api root!"}
