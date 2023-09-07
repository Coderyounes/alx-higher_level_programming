#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    if length == 0:
        print("0: arguments.")
    elif length == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(length - 1))
        for i in range(length):
            if i != 0:
                print("{}: {}".format(i, sys.argv[i]))
