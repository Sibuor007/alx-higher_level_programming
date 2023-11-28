#!/usr/bin/python3
for item in range(122, 96, -1):
    if item % 2:
        item = item - 32
    print("{:c}".format(item), end="")
