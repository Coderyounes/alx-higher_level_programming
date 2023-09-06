#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0 or n > len(str):
        return str
    else:
        newstr = ""
        for i in range(len(str)):
            if i != n:
                newstr += str[i]
        return newstr
