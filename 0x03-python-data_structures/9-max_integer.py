#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        biggest = my_list[0]
        for i in range(1, len(my_list)):
            if my_list[i] > biggest:
                biggest = my_list[i]
        return biggest
