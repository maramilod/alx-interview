#!/usr/bin/python3
"""
0-pascal_triangle.py
"""


def pascal_triangle(n):
    """
    Create a function that returns
    a list of lists of integers
    """
    if n <= 0:
        return []

    arr = [[1]]

    for i in range(1, n):
        new_row = [1]

        for j in range(1, i):
            new_row.append(arr[i-1][j-1] + arr[i-1][j])

        new_row.append(1)
        arr.append(new_row)

    return arr
