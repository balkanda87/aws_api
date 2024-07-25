#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Some health care"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

from fastapi import APIRouter

router = APIRouter()


@router.get("/api/", tags=["aws"])
async def read_aws_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/api/me", tags=["aws"])
async def read_aws_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/api/{username}", tags=["aws"])
async def read__user(username: str):
    return {"username": username}
