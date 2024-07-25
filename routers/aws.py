#!/usr/bin/env python

__author__ = "Balaji Kandasamy"
__copyright__ = "Copyright 2024, Some health care"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "someone"
__email__ = "balkanda87@outlook.com"

import boto3
import logging
from fastapi import APIRouter

router = APIRouter()
LOGGER = logging.getLogger(__name__)

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(funcName)s - %(message)s  ",
    datefmt="%d-%b-%y %H:%M:%S",
    level=logging.INFO,
)


@router.get("/api/s3", tags=["aws"])
async def connect_s3():
    """async function will create s3 session and retrun details."""

    session = boto3.Session(
        aws_access_key_id="YOUR_ACCESS_KEY_ID",
        aws_secret_access_key="YOUR_SECRET_ACCESS_KEY",
    )

    s3 = session.resource("s3")
    my_bucket = s3.Bucket("aws-client-demo-s3-bucket01")

    bucket_name = None
    file_list = []
    for my_bucket_object in my_bucket.objects.all():
        LOGGER.info(my_bucket_object.key)
        bucket_name = my_bucket_object.bucket_name
        file_list.append(my_bucket_object.key)

    if s3:
        LOGGER.info(s3)
    else:
        LOGGER.info("s3 object creation failed")

    return [{"bucket_name": bucket_name}, {"files_list": file_list}]


@router.get("/api/ec2", tags=["aws"])
async def connect_ec2():
    """async function will create s3 session and retrun details."""

    session = boto3.Session(
        aws_access_key_id="YOUR_ACCESS_KEY_ID",
        aws_secret_access_key="YOUR_SECRET_ACCESS_KEY",
    )

    # s3 = session.resource("ec2")
    # my_bucket = s3.Bucket("aws-client-demo-s3-bucket01")

    bucket_name = None
    file_list = []
    # for my_bucket_object in my_bucket.objects.all():
    #    LOGGER.info(my_bucket_object.key)
    #    bucket_name = my_bucket_object.bucket_name
    #    file_list.append(my_bucket_object.key)
    return [{"ec2_instance": "Didn't create"}, {"ip": "0.0.0.0"}]


@router.get("/api/", tags=["aws"])
async def read__user(username: str):
    return {"username": username}
