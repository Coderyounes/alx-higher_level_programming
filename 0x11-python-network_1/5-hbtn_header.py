#!/usr/bin/python3
"""
    Print a specifique header
        GET using requests module
        extract headers via '.headers' method
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]

    response = requests.get(url)
    header = response.headers
    print(header['X-Request-Id'])
