#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0 or my_list is None:
        return 0
    total = 0
    number = 0
    for tup in my_list:
        total += (tup[0] * tup[1])
        number += tup[1]
    return total / number
