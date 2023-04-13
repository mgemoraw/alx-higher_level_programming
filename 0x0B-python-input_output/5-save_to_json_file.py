#!/usr/bin/python3
"""
writes an object to text file using JSON
"""
import json

def save_to_file(my_obj, filename):
    """
    Writes an object to text file using JSON
    Args:
        my_obj (str): string object 
        filename (str): name of the file
    """
    with open(filename, "w") as file:
        json.dumps(my_obj, file)
