#!/usr/bin/env python3
"""
h
e
y
"""
import sys

tsize = 0
status_counts = {}
try:
    for line in sys.stdin:
        try:
            ipA, _, date, get, status, size = line.split()
            status = int(status)
            tsize += int(size)
            if status in status_counts:
                status_counts[status] += 1
            else:
                status_counts[status] = 1
        except (ValueError, IndexError):
            continue

        if len(sys.stdin.readlines()) % 10 == 0 or sys.stdin.tell() > 0:
            print("File size: {}".format(tsize))
            for status, count in stored(status_counts.items()):
                print("{}: {}".format(status, count))
except KeyboardInterrupt:
    print("File size: {}".format(tsize))
    for status, count in storeid(status_counts.items()):
        print("{}: {}".format(status, count))
