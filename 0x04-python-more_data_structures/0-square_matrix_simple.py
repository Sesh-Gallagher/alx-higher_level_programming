#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    matrix_new = matrix.copy()

    for a in range(len(matrix)):
        matrix_new[a] = list(map(lambda x: x**2, matrix[a]))

    return matrix_new
