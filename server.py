#!/usr/bin/env python

from flask import Flask, Response, send_file, jsonify, abort, request, redirect
import os, boto3, StringIO, urlparse
import simplejson as json
import subprocess

import config

app = Flask(__name__)


@app.route('/')
def home():
    """
    home page
    """
    return 'hello'


@app.route('/exif')
def exif():
    """
    home page
    """
    exiftool_output = subprocess.check_output(['bin/exiftool', '-ver'])
    return exiftool_output


@app.route('/metadata/<guid>')
def get_metadata(guid):
    """
    Endpoint to get metadata for a given GUID
    """
    print(guid)
    return jsonify({'hello': guid})


if __name__ == '__main__':
    app.run(processes=config.WORKERS, host='0.0.0.0', port=config.HTTP_PORT)