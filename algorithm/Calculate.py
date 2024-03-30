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

    def copy_result(self, frame):
        frame.clipboard_clear()
        frame.clipboard_append(f"Результат: {self.result}")
