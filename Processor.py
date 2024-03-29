from tkinter import *


#test
def calculate_matrices_sum(matrix1, matrix2, result_frame, size):
    for widget in result_frame.winfo_children():
        widget.destroy()

    result_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            try:
                value1 = float(matrix1[i][j].get())
                value2 = float(matrix2[i][j].get())
                row.append(value1 + value2)
            except ValueError:
                row.append(0)
        result_matrix.append(row)

    Label(result_frame, text="Result Matrix", font=("Arial", 16)).grid(row=0, columnspan=3)

    for i in range(len(result_matrix)):
        for j in range(len(result_matrix)):
            Label(result_frame, text=f"{result_matrix[i][j]:.2f}", width=5).grid(row=i + 1, column=j)
