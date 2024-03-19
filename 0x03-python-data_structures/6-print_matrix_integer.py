#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        for element in range(len(matrix[row])):
            print("{}".format(matrix[row][element]), end=" ")
            print(end="")
        print()
