import numpy as np

# nums = np.array([1, -2, 3, 4, -5])
# print(nums[nums > 0])


# room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
# room_2 = np.array([8, 9, 10, 11, 12, -13, -14])

# result = [
#     room_1[i] if room_1[i] >= 0 else room_2[i] if room_2[i] >= 0 else None
#     for i in range(0, 7)
# ]
# print(result)


# room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
# room_2 = np.array([8, 9, 10, 11, 12, -13, -14])

# result = [x if x >= 0 else y if y >= 0 else None for x, y in zip(room_1, room_2)]
# print(result)

# room_1 = np.array([1, 2, -3, 4, 5, 6, -7])
# room_2 = np.array([8, 9, 10, 11, 12, -13, -14])

# result = [
#     x if x >= 0 else y if y >= 0 else None for x, y in np.column_stack((room_1, room_2))
# ]
# print(result)

# mat2 = np.array([[6], [7]])

# mat3 = np.ones((1, 2))
# print(mat2 @ mat3)


# mat1 = np.array([[6], [7]])
# print(mat1)
# print(mat1.transpose())


def product(mat_a, mat_b):
    return mat_a @ mat_b, mat_a * mat_b


mat_1 = np.array([[1, 2], [3, 4]])
mat_2 = np.array([[5, 6], [7, 8]])

p_1, p_2 = product(mat_1, mat_2)
print(p_1)
print(p_2)
