#!/usr/bin/python3
def print_last_digit(number):
    n = number % 10
    if number < 0:
        number = -number
    print(f"{n}", end="")
    return (n)
