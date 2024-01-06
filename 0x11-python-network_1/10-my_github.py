#!/usr/bin/python3
"""
    Python Script Take you Credentials Dislay ID
"""
if __name__ == "__main__":
    import requests
    import sys

    u = sys.argv[1]
    password = sys.argv[2]
    header = {
        'Authorization': f'Bearer {password}'
        }

    r = requests.get('https://api.github.com/users/{}'.format(u), headers=header)
    if r.status_code == 200:
        r_json = r.json()
        print(r_json['id'])
    else:
        print('None')
