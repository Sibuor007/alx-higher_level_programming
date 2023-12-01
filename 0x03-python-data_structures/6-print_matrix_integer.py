#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j != len(matrix[i]) - 1:
                    var_1 = ' '
                else:
                    var_1 = ''
                print("{:d}".format(matrix[i][j]), end=var_1)
            print()
