#!/usr/bin/python3
"""Python script that takes your GitHub credentials(username and password)
and uses the GitHub API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(user, passwd)

    r = requests.get(url, auth=auth)

    print(r.json().get("id"))
