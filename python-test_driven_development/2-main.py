#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [5, 10, 20],
    [2, 5],
]
# ([[5, 10, 20], [2, 5, 4], -5)
print(matrix_divided(matrix, 5))
print(matrix)
