#!/usr/bin/python3
"""
JSON Respresentation of object
"""
import json


def from_json_string(my_str):
    """
    Returns a python object respresontationof JSON object
    """
    return json.loads(my_str)
