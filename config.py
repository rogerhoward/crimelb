#!/usr/bin/env python
import urlparse
import os

HTTP_PORT = 5000
WORKERS = 3

PROJECT_NAME = 'crimelb'

AWS_REGION = 'us-west-1'

S3_BASE_URL = 'https://s3-{}.amazonaws.com/'.format(AWS_REGION)

S3_BUCKET = '{}-data'.format(PROJECT_NAME)
S3_BUCKET_URL = urlparse.urljoin(S3_BASE_URL, S3_BUCKET)