import sympy as sp
from sympy import Matrix


def find_intersection_point_of_two_lines():
    A = sp.Matrix([[1, -1], [2, 3]])
    b = sp.Matrix([-2, 6])

    intersection_point = A.inv() * b

    print("Intersection point of the two lines:", list(intersection_point))


def find_intersection_of_three_planes():
    A = sp.Matrix([[1, -1, 0], [2, -1, -1], [1, 1, 1]])
    b = sp.Matrix([2, 3, 6])

    intersection_point = A.inv() * b
    print("Intersection point of three planes:", list(intersection_point))


def find_coefficient():
    A = sp.Matrix([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
    b = sp.Matrix([4, 3, 4])

    coefficients = A.inv() * b
    print("Coefficients a, b, c:", list(coefficients))


def find_coefficient_to_calculate_integral():
    A = sp.Matrix([[1, 0, 1], [1, 1, -2], [-2, 2, 1]])
    b = sp.Matrix([1, -3, 0])

    coefficients = A.inv() * b
    print("Coefficients a, b, c:", list(coefficients))


find_intersection_point_of_two_lines()
find_intersection_of_three_planes()
find_coefficient()
find_coefficient_to_calculate_integral()
