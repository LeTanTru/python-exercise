import numpy as np
import sympy as sp

X = np.array([[1, 0], [1, 1], [1, 2], [1, 3], [1, 4]])
Y = np.array([10, 8, 7, 5, 2])


XT = X.T

A1 = np.linalg.inv(np.dot(XT, X))
A2 = np.dot(XT, Y)
A = np.dot(A1, A2)

x = sp.symbols("x")


def get_fx(A):
    return A[0] + A[1] * x


errors = []
fx = get_fx(A)
print("fx=", fx)
for i in range(1, X.shape[0] + 1):

    errors.append((Y[i - 1] - fx.subs(x, X[i - 1][1])))

total_error = 0

for error in errors:
    total_error += error**2

print(total_error)

# print(np.dot(np.array(errors).T, np.array(errors)))
#
