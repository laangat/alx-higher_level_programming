#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for i in str:
        if i >= 'a' and i <='z':
            new_str = new_str + chr((ord(i) - 32))
        else:
            new_str = new_str + 1

    print("{}".format(new_str))
