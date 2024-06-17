#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.

Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
from urllib import request
from urllib import parse

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}

    data = parse.urlencode(value).encode("ascii")
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
