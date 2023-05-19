#!/usr/bin/python3
"""Writes text to a file and returns number of characters written"""


def write_file(filename="", text=""):
    """Writes text into the filename
    Args:
        filename (str): name of the file that text is to be written
        text (str): The text we are going to write
    Returns:
        The number of characters written to the file
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
