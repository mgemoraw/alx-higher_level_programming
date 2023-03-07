#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if (i % 3 == 0 and i % 5 == 0):
            print("{0}".format("FizzBuzz"), end=", ")
        elif (i % 3 == 0):
            print("{0}".format("Fizz"), end=", ")
        elif (i % 5 == 0):
            print("{0}".format("Buzz"), end=", ")
        else:
            print("{0}".format(i), end=", ")
    print("{0}".format("Buzz"))
