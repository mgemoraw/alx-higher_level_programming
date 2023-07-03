#!/usr/bin/python3
"""Adds all arguments to a Python list and save them to a file.
"""
import sys

if __name__ == "__main__":
    import json
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    file_name = "add_item.json"
    with open(file_name, "a+") as f:
        if f.tell() == 0:
            json.dump([], f)

    items = load_from_json_file("add_item.json")
    if len(sys.argv) > 1:
        items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
