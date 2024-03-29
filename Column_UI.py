from tkinter import *


def create_labeled_matrix(window, label_text):
    # Створення фрейму в переданому вікні
    frame = Frame(window)
    frame.pack(side=LEFT, padx=10, pady=10)

    # Створення лейбла в цьому фреймі
    label = Label(frame, text=label_text)
    label.grid(row=0, columnspan=3)

    # Створення поля вводу в цьому фреймі
    extra_entry = Entry(frame)
    extra_entry.grid(row=1, columnspan=3)

    # Створення матриці в цьому фреймі
    matrix = create_matrix(frame, 3, 3)

    # Створення кнопки для очищення матриці
    clear_button = Button(frame, text=f"Очистити {label_text.lower()}", command=lambda: clear_matrix(matrix))
    clear_button.grid(row=5, columnspan=3)

    return frame, label, extra_entry, matrix


def create_matrix(frame, rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            entry = Entry(frame, width=5)
            entry.grid(row=i + 2, column=j)  # Зсув рядків вниз на 2 для лейбла і поля вводу
            row.append(entry)
        matrix.append(row)
    return matrix


def clear_matrix(matrix):
    for row in matrix:
        for entry in row:
            entry.delete(0, END)
