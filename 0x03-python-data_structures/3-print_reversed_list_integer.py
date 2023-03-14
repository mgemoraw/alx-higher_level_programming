#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list != None:
        my_list.reverse()
        for i in range(len(my_list)):
            print("{:d}".format(my_list[i]))
    else:
        print("{}".format(None))


my_list = None
print_reversed_list_integer(my_list)


my_list = [1, 3, 5, 7]
print_reversed_list_integer(my_list)

print(my_list)