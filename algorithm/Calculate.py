import numpy as np

from model.Side import Side
from tkinter import *


class Calculate:
    def __init__(self):
        super().__init__()
        self.result = []

    def invoke(self, matrix_1: Side, matrix_2: Side, frame):
        result_matrix = []

        for i in range(len(matrix_1.matrix)):
            row = []
            for j in range(len(matrix_1.matrix)):
                row.append(matrix_1.get_converted_as_np()[i][j] + matrix_2.get_converted_as_np()[i][j])
            result_matrix.append(row)

        self.result = result_matrix

        Label(frame, text="Result of sum").grid(row=0, column=1, sticky="NSEW")
        for i in range(len(result_matrix)):
            row = result_matrix[i]
            for j in range(len(row)):
                label = (Label(frame, text=row[j]))
                label.grid(row=i + 1, column=j, sticky="NSEW")
        Button(frame, text="Копіювати результат", command=lambda: self.copy_result(frame)).grid(column=1)

    #in progress
    def foo(self, matrix_x, matrix_alice, matrix_bob):
        alice = np.array(matrix_alice.get_converted_as_np())
        bob = np.array(matrix_bob.get_converted_as_np())
        x = np.array(matrix_x.get_converted_as_np())
        print(f"alice {alice}")
        print(f"bob {bob}")
        print(f"x {x}")


    def matrix_power_mod(self, matrix, power, field_size):
        result = np.eye(matrix.shape[0], dtype=int)  # Одинична матриця
        for _ in range(power):
            result = (np.dot(result, matrix) % field_size).astype(int)
        return result

    def inverse_mod_matrix(self, matrix, field_size):
        det = int(np.round(np.linalg.det(matrix)))
        det_inv = pow(det, -1, field_size)
        matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % field_size
        return matrix_mod_inv

    def copy_result(self, frame):
        frame.clipboard_clear()
        frame.clipboard_append(f"Результат: {self.result}")
