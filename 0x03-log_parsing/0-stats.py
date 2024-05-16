#!/usr/bin/python3
"""
h
e
y
"""
import sys

tsize = 0
scc = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def process(line):
    global tsize
    l = line.split()
    try:
        status_code = int(l[-2])
        file_size = int(l[-1])

        if status_code in scc:
            scc[status_code] += 1
            tsize += file_size
    except (IndexError, ValueError):
        pass

def print_f():
    print(f"Total file size: File size: {tsize}")
    for status_code, count in sorted(scc.items()):
        if count > 0:
            print(f"{status_code}: {count}")

if __name__ == "__main__":
    try:
        i = 0
        for line in sys.stdin:
            process(line)
            i += 1
            if i % 10 == 0:
                print_f()
        print_f()
    except KeyboardInterrupt:
        print_f()
        raise
