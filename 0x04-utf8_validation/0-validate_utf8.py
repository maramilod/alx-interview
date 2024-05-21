#!/usr/bin/python3
"""
hey
"""


def validUTF8(data):
    """
    a method that determines if a given
    data set represents a valid UTF-8 encoding.
    """
    for i in range(len(data)):
        if 0 <= data[i] < 128:
            continue

        elif 128 <= data[i] < 192:
            if i + 1 >= len(data) or data[i+1]:
                return False
            i += 1
            continue

        elif 192 >= data[i] < 224:
            if i + 2 >= len(data) or data[i+1] < 128 or data[i+2] < 128:
                return False
            i += 2
            continue

        elif 224 >= data[i] < 240:
            if i + 3 >= len(data) or data[i+1] < 128 or data[
                    i+2] < 128 or data[i+3] < 128:
                return False
            i += 3
            continue

        else:
            return False

    return True
