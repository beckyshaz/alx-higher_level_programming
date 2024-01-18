#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sumsint = 0
    for i in range(1, len(argv)):
        sumsint += int(argv[i])
    print("{}".format(sumsint))

