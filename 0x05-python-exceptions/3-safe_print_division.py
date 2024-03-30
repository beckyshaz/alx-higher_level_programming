#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return None
    else:
        return result
    finally:
        try:
            print("Inside result: {}".format(a / b))
            print("Inside result: {}".format(None))
        except ZeroDivisionError:
            return None

