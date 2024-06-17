#!/usr/bin/python3
""" take url and display X-Request-Id """

import sys
from urllib import request

if __name__ == "__main__":
    url = sys.argv[1]
    request_url = request.Request(url)
    with request.urlopen(request_url) as response:
        print(dict(response.headers).get("X-Request-Id"))
