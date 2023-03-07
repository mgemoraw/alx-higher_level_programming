#!/usr/bin/python3
def uppercase(str):
    cstr = ""
    for c in str:
        if (ord(c) >= 97 and ord(c) <= 123):
            cstr +=chr(ord(c) - 32)
        else:
            cstr += c
    print(cstr)
