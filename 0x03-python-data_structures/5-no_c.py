#!/usr/bin/python3
def no_c(my_string):
    no_cs = ""
    for s in my_string:
        if s != 'c' and s != 'C':
            no_cs = no_cs + s
    return no_cs
