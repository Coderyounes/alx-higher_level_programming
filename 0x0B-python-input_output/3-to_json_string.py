#!/usr/bin/python3

import json


"""Function return json represetation of the object"""


def to_json_string(my_obj):
    """
    in this Code we import json library to
    use json dump and print the json representation of the object
    """
    return json.dumps(my_obj)
