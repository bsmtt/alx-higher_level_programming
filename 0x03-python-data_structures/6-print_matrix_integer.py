#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for row in matrix:
        if len(row) == 0:
            print()
        for num in row:
            print("{:d}".format(num), end=" " if row[-1] != num else "\n")
