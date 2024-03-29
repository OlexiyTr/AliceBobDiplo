from tkinter import *


def display_result_matrix(result_frame, result_matrix):

    for widget in result_frame.winfo_children():
        widget.destroy()

    for i, row in enumerate(result_matrix):
        for j, value in enumerate(row):
            Label(result_frame, text=f"{value:.2f}", width=5).grid(row=i, column=j)


def calculate_and_display_matrices_sum(matrix1, matrix2, result_frame):
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            try:
                value1 = float(matrix1[i][j].get())
                value2 = float(matrix2[i][j].get())
                result_matrix[i][j] = value1 + value2
            except ValueError:
                pass

    display_result_matrix(result_frame, result_matrix)
