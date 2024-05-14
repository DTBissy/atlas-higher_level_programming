#!/usr/bin/python3
"""This is a function for to divide a matrix"""

def matrix_divided(matrix, div):
    """This checks if number is a integer or float

    Args:
        matrix (_type_): The matrix we hold
        div (_type_): What the matrix is divided for

    Raises:
        TypeError: For if the list isnt a list with integers or floats
        TypeError: For if the list length isnt the same length as the first
        TypeError: For if the value isnt a number or float
        ZeroDivisionError: For if the number is a zero

    Returns:
        div
    """
    if not all(isinstance(row, list) and all(isinstance(element, (float, int)
    ) for element in row) for row in matrix):
        raise TypeError("Matrix must be a matrix (list of list) of integers/floats")

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not(isinstance(div, (int, float))):
        raise TypeError("div must be number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return (new_matrix)