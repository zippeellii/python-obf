#!/usr/bin/env python
"""Hello."""
# -*- coding: utf-8 -*-
import urllib
import urllib2
import json
import sys
import os

API_URL = "http://www.scurtu.it/apis/documentSimilarity"


def call_api(url, input_object):
    """Hello."""
    params = urllib.urlencode(input_object)
    f = urllib2.urlopen(url, params)
    response = f.read()
    response_object = json.loads(response)
    return response_object


if __name__ == "__main__":
    input_dict = {}

    dir_path = os.path.dirname(os.path.realpath(__file__))

    with open(dir_path + '/test_script.py') as c:
        data = c.read()
        input_dict['doc1'] = data

    stdin = sys.argv[-1]
    with open(stdin) as c:
        data = c.read()
        input_dict['doc2'] = data

    finalResponse = call_api(API_URL, input_dict)

    print finalResponse
