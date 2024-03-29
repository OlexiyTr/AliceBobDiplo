import numpy as np
from tkinter import *


# Функція для обчислення оберненої матриці в скінченному полі
def inverse_mod_matrix(matrix, field_size):
    det = int(np.round(np.linalg.det(matrix)))  # Обчислюємо детермінант матриці
    det_inv = pow(det, -1, field_size)  # Обчислюємо обернене число для детермінанта
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % field_size
    return matrix_mod_inv


# Функція для піднесення матриці до степеня в скінченому полі
def matrix_power_mod(matrix, power, field_size):
    result = np.eye(len(matrix), dtype=int)  # Одинична матриця
    for _ in range(int(power)):
        result = (np.dot(result, matrix) % field_size).astype(int)
    return result

def foo(matrix_alice, matrix_bob, X, a, b, field_size, result_frame):
    alice = ui_to_core(matrix_alice)
    bob = ui_to_core(matrix_bob)
    x = ui_to_core(X)

    # Аліса обчислює (T' * X^b * T^-1)^a
    Alice_computation = matrix_power_mod(
        np.dot(np.dot(bob, matrix_power_mod(x, int(b), field_size)), inverse_mod_matrix(alice, field_size)),
        a,
        field_size
    )

    # Боб обчислює (T * X^a * T'^-1)^b
    Bob_computation = matrix_power_mod(
        np.dot(np.dot(alice, matrix_power_mod(x, int(a), field_size)), inverse_mod_matrix(bob, field_size)),
        b,
        field_size
    )

    Label(result_frame, text="Alice_computation", font=("Arial", 16)).grid(row=0, columnspan=3)

    for i in range(len(Alice_computation)):
        for j in range(len(Alice_computation)):
            Label(result_frame, text=f"{Alice_computation[i][j]:.2f}", width=5).grid(row=i + 1, column=j)

    Label(result_frame, text="Bob_computation", font=("Arial", 16)).grid(row=0, columnspan=3)

    for i in range(len(Bob_computation)):
        for j in range(len(Bob_computation)):
            Label(result_frame, text=f"{Bob_computation[i][j]:.2f}", width=5).grid(row=i + 1, column=j)

    # return Alice_computation, Bob_computation


def ui_to_core(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(matrix[i][j].get())

        result.append(row)
    return np.array(result)


# Приклад ініціалізації матриць та параметрів
# T = np.array([[1, 2], [3, 4]])
# T_prime = np.array([[4, 3], [2, 1]])
# X = np.array([[1, 0], [0, 1]])
# a = 3
# b = 5
# field_size = 7
#
# # Виконуємо алгоритм
# Alice_computation, Bob_computation = non_commutative_diffie_hellman(T, T_prime, X, a, b, field_size)
#
# print("Аліса обчислила: ")
# print(Alice_computation)
# print("\nБоб обчислив: ")
# print(Bob_computation)
