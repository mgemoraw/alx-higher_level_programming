import requests
import sys


# url = sys.argv[1]
# username = sys.argv[2]
# password = sys.argv[3]


payload = {'username': 'corey', 'password': 'testing'}

r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()
print(r_dict['form'])