#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.

Usage: ./3-error_code.py <URL>
  - Displays the body of the response.
"""

import sys
from urllib import request
from urllib import parse
from urllib import error

if __name__ == "__main__":
    url = sys.argv[1]

    req = request.Request(url)
    try:
        with request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
