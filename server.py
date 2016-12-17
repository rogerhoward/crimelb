#!/usr/bin/env python

from flask import Flask, Response, send_file, jsonify, abort, request, redirect
import os, boto3, StringIO, urlparse
import simplejson as json

import config

app = Flask(__name__)


@app.route('/')
def home():
    """
    home page
    """
    return 'hello'


@app.route('/metadata/<guid>')
def get_metadata(guid):
    """
    Endpoint to get metadata for a given GUID
    """
    print(identifier)
    return jsonify({'hello': identifier})


if __name__ == '__main__':
    app.run(processes=workers, host='0.0.0.0', port=port)