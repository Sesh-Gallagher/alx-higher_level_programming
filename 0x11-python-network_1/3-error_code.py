#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL
displays the body of the response : urllib.error.HTTPError."""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
