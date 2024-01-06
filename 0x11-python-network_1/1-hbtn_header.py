#!/usr/bin/python3
import sys
import urllib.request

"""
    Extraxt Header using urlib
"""

with urllib.request.urlopen(sys.argv[1]) as response:
    html = response.read()
    headers = response.headers
    print(headers['X-Request-Id'])
