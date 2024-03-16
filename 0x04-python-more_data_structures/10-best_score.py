#!/usr/bin/python3
def best_score(a_dictionary):
    for i in  a_dictionary:
        if i == None:
            return None
    return max(a_dictionary, key=a_dictionary.get) 
