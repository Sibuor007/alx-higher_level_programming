#!/usr/bin/python3
for item in range(97, 123):
    if (item == 101) or (item == 113):
        continue
    print(chr(item).format(), end="")
