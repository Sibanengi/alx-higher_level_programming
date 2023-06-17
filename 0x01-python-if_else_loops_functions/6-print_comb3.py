#!/usr/bin/python3
for n in range(0, 10):
    for i in range(0, 10):
        if n < i and n != 8:
            print('{:d}{:d}, '.format(n, i), end='')
        if n < i and n == 8:
            print('{:d}{:d}'.format(n, i))
