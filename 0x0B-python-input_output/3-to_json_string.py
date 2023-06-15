#!/usr/bin/python3
"""Writes string to Json"""
import json


def to_json_string(my_obj):
    """
    changes text to json file format
    Args:
        my_obj (str): text object
    Returns:
        The json file format
    """
    return json.dumps(my_obj)
