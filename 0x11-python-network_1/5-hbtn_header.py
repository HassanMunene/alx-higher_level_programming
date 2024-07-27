#!/usr/bin/python3
"""
take in a URL send a request to the URl
display the value of the variable
X-Request-Id in the response header
"""
import requests

import sys
if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url)
    response_id = response.headers.get("X-Request-Id")
    print(response_id)
    pass
