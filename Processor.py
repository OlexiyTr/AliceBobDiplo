from tkinter import *


def calculate_matrices_sum(matrix1, matrix2, result_frame):
    for widget in result_frame.winfo_children():
        widget.destroy()

    result_matrix = []
    for i in range(2):
        row = []
        for j in range(2):
            try:
                value1 = float(matrix1[i][j].get())
                value2 = float(matrix2[i][j].get())
                row.append(value1 + value2)
            except ValueError:
                row.append(0)
        result_matrix.append(row)

    Label(result_frame, text="Result Matrix", font=("Arial", 16)).grid(row=0, columnspan=3)
    for i, row_values in enumerate(result_matrix):
        for j, value in enumerate(row_values):
            Label(result_frame, text=f"{value:.2f}", width=5).grid(row=i+1, column=j)
