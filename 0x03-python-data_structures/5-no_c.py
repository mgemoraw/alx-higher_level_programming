#!/usr/bin/python3
# function removed c or C
def no_c(my_string):
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] in "cC":
            continue
        else:
            new_str += my_string[i];
    return new_str
