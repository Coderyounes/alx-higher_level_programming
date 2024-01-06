#!/usr/bin/python3
"""
    Handling Error with try & expect
"""

if __name__ == '__main__':
    import requests
    import sys

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
