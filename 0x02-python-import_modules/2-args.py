#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arguments = "{:d} argument"
    length = len(sys.argv) - 1

    if length == 0:
        arguments += 's.'
    elif length == 1:
        arguments += ':'
    else:
        arguments += 's:'
    print(arguments.format(length))

    for i in range(length):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
