#!/usr/bin/python3
# 6-print_matrix_integer.py

def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    for digit1 in range(0, 10):
        for digit2 in range(digit1 + 1, 10):
            if digit1 == 8 and digit2 == 9:
                print("{}{}".format(digit1, digit2))
            else:
                print("{}{}".format(digit1, digit2), end=", ")
