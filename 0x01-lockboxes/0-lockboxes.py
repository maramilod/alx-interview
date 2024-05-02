#!/usr/bin/python3
"""
hey
"""


def canUnlockAll(boxes):
    """
    determines if all the boxes can be opened.
    """
    allb = len(boxes)
    explored = []
    keys = [0]

    while len(explored) != allb and len(keys) != 0:
        for key in boxes[keys[0]]:
            if key not in explored and key not in keys and key < allb:
                keys.append(key)
        explored.append(keys.pop(0))

    return len(explored) == allb
