#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """Returns a new matrix
    """

    if not isinstance(matrix, list) or not matrix[0] or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
            "of integers/floats")

    for item_row in matrix:
        if len(item_row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                "of integers/floats")
        for item_col in item_row:
            if type(item_col) is not int and type(item_col) is not float:
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")

    row_len = []
    for item_row in matrix:
        row_len.append(len(item_row))
    if not all(item_col == row_len[0] for item_col in row_len):
        raise TypeError("Each item_row of the matrix must have the same size")

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    final_matrix = [[round(item_col / div, 2) for item_col in item_row] for item_row in matrix]

    return final_matrix
