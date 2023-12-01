#!/usr/bin/python3
"""Script that takes in a URL, sends a request to the URL
and displays the value of X-Request-Id
- uses urlib and sys packages
- Importing other package not allowed
- Value of this variable is different for each request
"""


if __name__ == '__main__':
    import urllib.request
    import sys

    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(dict(response.headers).get("X-Request-Id"))
