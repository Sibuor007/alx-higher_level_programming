#!/usr/bin/python3
def magic_calculation(a, b):
    num = 0
    for item in range(1, 3):
        try:
            if item > a:
                raise Exception('Too far')
            num += a ** b / item
        except Exception:
            num = b + a
            break
    return num
