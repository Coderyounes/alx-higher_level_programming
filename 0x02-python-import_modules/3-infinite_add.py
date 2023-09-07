#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    num = 0
    length = len(sys.argv)

    for i in range(1, length):
        num += int(sys.argv[i])
    print(num)
