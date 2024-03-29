#!/usr/bin/python3
"""Function for reading (loading) JSON file."""
import json


def load_from_json_file(filename):
    """Creates a Python object from a JSON file."""
    with open(filename) as file:
        return json.load(file)
