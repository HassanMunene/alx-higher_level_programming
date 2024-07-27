#!/usr/bin/python3
"""
take in a URL and an email address
send a POST request to the passed URL
with the email as a parameter
and finally displays the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    body = response.text
    print(body)
    pass
