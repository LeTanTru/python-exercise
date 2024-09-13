import numpy as np


def find_intersection_point_of_two_lines():
    A = np.array([[1, -1], [2, 3]])
    b = np.array([-2, 6])

    intersection_point = np.linalg.inv(A).dot(b)

    print("Intersection point of the two lines:", intersection_point)


def find_intersection_of_three_planes():
    A = np.array([[1, -1, 0], [2, -1, -1], [1, 1, 1]])
    b = np.array([2, 3, 6])

    intersection_point = np.linalg.inv(A).dot(b)
    print("Intersection point of three planes:", intersection_point)


def find_coefficient():
    A = np.array([[1, 1, 1], [4, 2, 1], [9, 3, 1]])
    b = np.array([4, 3, 4])

    coefficients = np.linalg.inv(A).dot(b)
    print("Coefficients a, b, c:", coefficients)


def find_coefficient_to_calculate_integral():
    A = np.array([[1, 0, 1], [1, 1, -2], [-2, 2, 1]])
    b = np.array([1, -3, 0])

    coefficients = np.linalg.inv(A).dot(b)
    print("Coefficients a, b, c:", coefficients)


find_intersection_point_of_two_lines()
find_intersection_of_three_planes()
find_coefficient()
find_coefficient_to_calculate_integral()
