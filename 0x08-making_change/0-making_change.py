#!/usr/bin/python3
"""
h
e
y
"""


def makeChange(coins, total):
    """
    coins is a list of the values of the coins in your possession
    fewest number of coins needed to meet tota
    """
    result = 0
    if total == 0:
        return 0
    coins.sort(reverse=True)

    for c in coins:
        while c <= total:
            total -= c
            result += 1
    if total == 0:
        return result
    return -1
