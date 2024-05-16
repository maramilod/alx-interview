#!/usr/bin/env python3
"""
h
e
y
"""
import sys

tsize = 0
statusc = {}
try:
    for line in sys.stdin:
        try:
            ipA, _, date, get, status, size = line.split()
            status = int(status)
            tsize += int(size)

            if  status in statusc:
                statusc[status] += 1
            else:
                statusc[status] = 1
        except ValueError:
            pass

        if len(sys.stdin.readlines()) % 10 == 0 or sys.stdin.tell() > 0:
            print("File size: {}".format(tsize))
            for status, count in stored(tatusc.items()):
                print("{}: {}".format(status, count))
except KeyboardInterrupt:
    print("\nInterrupted by user.")
