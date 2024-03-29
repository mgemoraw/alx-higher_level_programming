#!/usr/bin/python3
"""A script that takes in a URL  and opena an email,
sends a POST request to the passed URL with the email as a parameter
- displays the body of the response
- The email must be sent in the email variable
- Must use the packages urllib and sys
"""


if __name__ == "__main__":
    import sys
    import urllib.parse
    import urllib.request

    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(url, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
