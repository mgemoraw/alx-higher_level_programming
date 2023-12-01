import requests
import sys


url = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]


req = requests.get(url, auth=(username, password))

print(req.status_code)
