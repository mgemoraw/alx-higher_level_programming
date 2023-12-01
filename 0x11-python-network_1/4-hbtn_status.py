#!/usr/bin/python3
"""
A Script that takes in URL,
sends a request to the URL and displays the body of the response
decoded in utf-8
"""
import requests


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    req = requests.get(url)
    data = req.text

    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
