#!/usr/bin/python3
"""
    Send Post request using urllib
            parse post-data as Dictionary
            pass to urlencode
            make it  in asci form
            send the request
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys
    url = sys.argv[1]
    email = {'email': sys.argv[2]}
    postdata = urllib.parse.urlencode(email)
    data = postdata.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as r:
        print("Your email is: {}".format(email['email']))
