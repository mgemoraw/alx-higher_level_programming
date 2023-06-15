#!/usr/bin/python3
"""
Returns String Respresentation of JSON object
"""
import json


def from_json_string(my_str):
    """
    Returns a python object respresontationof JSON object
    """
    return json.loads(my_str)
