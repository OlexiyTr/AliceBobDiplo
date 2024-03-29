from tkinter import *

import numpy as np


# Функція для обчислення оберненої матриці в скінченному полі
def inverse_mod_matrix(matrix, field_size):
    det = int(np.round(np.linalg.det(matrix)))  # Обчислюємо детермінант матриці
    det_inv = pow(det, -1, field_size)  # Обчислюємо обернене число для детермінанта
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % field_size
    return matrix_mod_inv


# Функція для піднесення матриці до степеня в скінченому полі
def matrix_power_mod(matrix, power, field_size):
    result = np.eye(matrix.shape[0], dtype=int)  # Одинична матриця
    for _ in range(power):
        result = (np.dot(result, matrix) % field_size).astype(int)
    return result


def foo(matrix_alice, matrix_bob, X, a, b, field_size, result_frame):
    alice = ui_to_core(matrix_alice)
    bob = ui_to_core(matrix_bob)
    x = ui_to_core(X)

    matrix_alice_result = matrix_power_mod(
        np.dot(np.dot(bob, matrix_power_mod(x, int(b), field_size)), inverse_mod_matrix(alice, field_size)),
        a,
        field_size
    )

    matrix_bob_result = matrix_power_mod(
        np.dot(np.dot(alice, matrix_power_mod(x, int(a), field_size)), inverse_mod_matrix(bob, field_size)),
        b,
        field_size
    )

    show_result(matrix_alice_result, matrix_bob_result, result_frame)


def show_result(matrix_alice, matrix_bob, result_frame):
    Label(result_frame, text="Alice_computation", font=("Arial", 16)).grid(row=0, columnspan=3)

    for i in range(len(matrix_alice)):
        for j in range(len(matrix_alice)):
            Label(result_frame, text=f"{matrix_alice[i][j]:.2f}", width=5).grid(row=i + 1, column=j)

    Label(result_frame, text="Bob_computation", font=("Arial", 16)).grid(row=0, columnspan=3)

    for i in range(len(matrix_bob)):
        for j in range(len(matrix_bob)):
            Label(result_frame, text=f"{matrix_bob[i][j]:.2f}", width=5).grid(row=i + 1, column=j)


def ui_to_core(matrix):
    result = []
    for i in range(len(matrix)):
        row = []
        for j in range(len(matrix)):
            row.append(int(matrix[i][j].get()))

        result.append(row)
    return np.array(result)
