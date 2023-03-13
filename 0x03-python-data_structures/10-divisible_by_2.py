#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = [val % 2 == 0 for val in my_list]
    return (new_list)
