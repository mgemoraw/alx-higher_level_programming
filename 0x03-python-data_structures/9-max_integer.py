#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    get_max = my_list[0]
    for i in range(0, len(my_list)):
        if get_max < my_list[i]:
            get_max = my_list[i]
        else:
            continue
    return (get_max)
