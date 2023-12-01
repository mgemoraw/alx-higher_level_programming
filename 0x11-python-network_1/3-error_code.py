#!/usr/bin/python3
"""
A Script that takes in URL,
sends a request to the URL and displays the body of the response
decoded in utf-8
"""
from urllib import request, error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('UTF-8'))
    except error.HTTPError as err:
        print('Error code:', err.code)
