#!/usr/bin/python3
"""
    first usage of urllib
        parse type
        parse content
        parse content in utf-8
"""
if __name__ == '__main__':
    import urllib.request

    with urllib.request.urlopen('https://intranet.alxswe.com/status') as r:
        html = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
