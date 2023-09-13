#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return "None"
    else:
        maxvalue = 0
        for k, v in a_dictionary.items():
            if maxvalue < v:
                maxvalue = v
                maxkey = k
        return maxkey
