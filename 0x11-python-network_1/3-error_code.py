#!/usr/bin/python3
"""
take in a URL send a request to the URL
and display the body of the response
"""
import urllib.request
import sys
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
        pass
