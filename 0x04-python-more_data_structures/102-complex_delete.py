#!/urs/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary:
        new_dicts = {key: val for key, val in a_dictionary.items() if val != value}
        return new_dicts
    else:
        return a_dictionary
