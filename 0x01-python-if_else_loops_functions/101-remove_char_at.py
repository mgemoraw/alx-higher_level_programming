#!/usr/bin/python3
def remove_char_at(str, n):
    nstr = ""
    for i in range(len(str)):
        if (i == n):
            continue;
        else:
            nstr += str[i]
    print("{0}".format(nstr))
