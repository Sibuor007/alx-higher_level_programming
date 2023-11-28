#!/usr/bin/python3
def uppercase(str):
    for item in str:
        if ord("a") <= ord(item) <= ord("z"):
            item = chr(ord(item) - 32)
        print("{:s}".format(item), end="")
    print()
