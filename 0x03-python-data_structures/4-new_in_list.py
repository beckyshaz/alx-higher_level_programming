#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    mylist = my_list.copy()
    if idx < 0:
        return mylist
    if idx > len(my_list) - 1:
        return mylist
    mylist[idx] = element
    return mylist
    
