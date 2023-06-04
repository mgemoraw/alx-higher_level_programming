#!/usr/bin/python3
"""prints text 2 new lines"""


def text_indentation(text):
    """prints text with new lines after ., ?, : """
    flag = False
    if not (isinstance(text, str)):
        raise TypeError("text must be a string")

    for c in text:
        if not (c in ".?:"):
            if (flag is False):
                print(c, end="")
            flag = False
        else:
            print(c, end="$\n")
            print("$")
            flag = True
