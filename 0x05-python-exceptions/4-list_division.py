#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    length = []
    for i, j in zip(my_list_1, my_list_2):
        try:
            length.append(i/j)
        except (RuntimeError, ValueError):
            length.append(0)
            pass
        except TypeError:
            length.append(0)
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
            length.append(0)
        except IndexError:
            print("out of range")
            length.append(0)
        finally:
            pass
    return length



"""TEST CODE
my_l_1 = [10, 8, 4]
my_l_2 = [2, 4, 4]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

print("--")

my_l_1 = [10, 8, 4, 4]
my_l_2 = [2, 0, "H", 2, 7]
result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
print(result)

"""
