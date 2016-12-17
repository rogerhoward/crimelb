#!/usr/bin/env python

import os
from sh import exiftool
import simplejson as json


def get(path):
    """Extract the metadata from a file using exiftool.

    All available groups and fields will be extracted.

    Args:
        file_path (string): File path from which to extract metadata.

    Returns:
        dictonary: False otherwise.

    """
    print ('metadata, from: {}'.format(path))
    if os.path.isfile(path):
        output = exiftool('-m', '-G', '-struct', '-s', '-s', '-g', '-json', path).replace('\\u0000','')
        return json.loads(output)[0]
    else:
        return None
