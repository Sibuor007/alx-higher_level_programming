#!/usr/bin/python3
"""Pascal's Triangle"""

def pascal_triangle(n):
    """ Pascal's Triangle function body
    """
    if n <= 0:
        return []

    tr_angles = [[1]]
    while len(tr_angles) != n:
        item_ = tr_angles[-1]
        temp_ = [1]
        for k in range(len(item_) - 1):
            temp_.append(item_[k] + item_[k + 1])
        temp_.append(1)
        tr_angles.append(temp_)
    return
