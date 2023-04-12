#!/usr/bin/python3
"""Appends text to a file and returns number of characters appended"""


def append_write(filename="", text=""):
    """Appends the value of text into tile and returns the number of chars appended
    Args:
        filename (str): The name of the file that text is going to be appended
        text (str): the input string text
    Returns:
        The number of characters appended to the file
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
