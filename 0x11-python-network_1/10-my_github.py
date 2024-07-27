#!/usr/bin/python3
"""
will take my Github credetials i.e username and PAT
and use Github api to display my id
"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get("https://api.github.com/user", auth=auth)
    json_resp = response.json()
    id = json_resp.get('id')
    print(id)
    pass
