#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    i = 0
    lon = len(str)
    if n < 0 or lon < n:
        return str
    else:
        while lon > i:
            if n == i:
                i += 1
                continue
            s += str[i]
            i += 1
        return s
