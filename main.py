import numpy as np


from App import App


def foo(matrix):
    field_size = 17

    determinant = np.linalg.det(matrix) % field_size
    print(f"determinant: {determinant}")

    _determinant = mod_inverse(int(determinant), field_size)
    print(f"взаємно просте: {_determinant}")

    adj = matrix_adjugate(matrix)
    print(f"матриця ад'юнкт {adj}")

    new_matrix = np.mod(_determinant * adj, field_size)
    print(new_matrix)



def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def mod_inverse(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception('Мультиплікативне обернене не існує')
    else:
        return x % m

def calc_cofactor(matrix, row, col):
    minor = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
    cofactor = ((-1) ** (row + col)) * np.linalg.det(minor)
    return cofactor

def matrix_adjugate(matrix):
    if matrix.size == 1:
        return np.array([[1]])

    adjugate_matrix = np.zeros(matrix.shape)

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            adjugate_matrix[row, col] = calc_cofactor(matrix, row, col)
    return adjugate_matrix.T


if __name__ == "__main__":
    foo(np.array([[12, 2], [5, 14]]))
    App(3)
