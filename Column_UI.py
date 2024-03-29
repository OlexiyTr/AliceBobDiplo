from tkinter import *


def create_labeled_matrix(window, label_text, size, value_matrix, value_number):
    frame = Frame(window)
    frame.pack(side=LEFT, padx=10, pady=10)

    label = Label(frame, text=label_text)
    label.grid(row=0, columnspan=3)

    extra_entry = Entry(frame)
    extra_entry.grid(row=1, columnspan=3)

    matrix = create_matrix(frame, size)

    clear_button = Button(frame, text=f"Очистити {label_text.lower()}", command=lambda: clear_matrix_and_entry(extra_entry, matrix))
    clear_button.grid(row=5, columnspan=3)

    predefine_button = Button(frame, text=f"Вставити значення",
                          command=lambda: setup_default(matrix, value_matrix, extra_entry, value_number))
    predefine_button.grid(row=6, columnspan=3)

    return frame, label, extra_entry, matrix


def create_example_matrix(window, label_text, size, value_matrix):
    frame = Frame(window)
    frame.pack(side=LEFT, padx=10, pady=10)

    label = Label(frame, text=label_text)
    label.grid(row=0, columnspan=3)

    matrix = create_matrix(frame, size)

    clear_button = Button(frame, text=f"Очистити {label_text.lower()}", command=lambda: clear_matrix(matrix))
    clear_button.grid(row=5, columnspan=3)

    predefine_button = Button(frame, text=f"Вставити значення",
                              command=lambda: setup_matrix(matrix, value_matrix))
    predefine_button.grid(row=6, columnspan=3)

    return frame, label, matrix


def create_matrix(frame, size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            entry = Entry(frame, width=5)
            entry.grid(row=i + 2, column=j)
            row.append(entry)
        matrix.append(row)
    return matrix


def clear_matrix_and_entry(e, matrix):
    e.delete(0, END)
    clear_matrix(matrix)

def setup_default(matrix, value_matrix, extra_entry, value_number):
    extra_entry.delete(0, END)
    extra_entry.insert(0, str(value_number))
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j].delete(0, END)
            matrix[i][j].insert(0,str(value_matrix[i][j]))

def setup_matrix(matrix, value_matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j].delete(0, END)
            matrix[i][j].insert(0,str(value_matrix[i][j]))


def clear_matrix(matrix):
    for row in matrix:
        for entry in row:
            entry.delete(0, END)

def clear_all(matrix1, matrix2):
    clear_matrix(matrix1)
    clear_matrix(matrix2)
