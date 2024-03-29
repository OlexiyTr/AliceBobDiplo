from tkinter import *


class Side:
    def __init__(self, window, title, size, value_matrix, value_number):
        super().__init__()
        frame = Frame(window)
        frame.pack(side=LEFT, padx=10, pady=10)
        label = Label(frame, text=title)

        label.grid(row=0, columnspan=3)

        extra_entry = Entry(frame)

        extra_entry.grid(row=1, columnspan=3)

        matrix = self.create_matrix(frame, size)

        clear_button = Button(frame, text=f"Очистити {title.lower()}",
                              command=lambda: self.clear_matrix_and_entry(extra_entry, matrix))
        clear_button.grid(row=5, columnspan=3)

        predefine_button = Button(frame, text=f"Вставити значення",
                                  #command=lambda: self.setup_default(matrix, value_matrix, extra_entry, value_number))
                                  command=lambda: self.setup_default(matrix, value_matrix, extra_entry, value_number))
        predefine_button.grid(row=6, columnspan=3)

    def create_matrix(self, frame, size):
        matrix = []
        for i in range(size):
            row = []
            for j in range(size):
                entry = Entry(frame, width=5)
                entry.grid(row=i + 2, column=j)
                row.append(entry)
            matrix.append(row)
        return matrix

    def clear_matrix_and_entry(self, e, matrix):
        e.delete(0, END)
        self.clear_matrix(matrix)

    def clear_matrix(self, matrix):
        for row in matrix:
            for entry in row:
                entry.delete(0, END)

    def clear_matrix_and_entry(self, e, matrix):
        e.delete(0, END)
        self.clear_matrix(matrix)

    def setup_default(self, matrix, value_matrix, extra_entry, value_number):
        extra_entry.delete(0, END)
        extra_entry.insert(0, str(value_number))
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                matrix[i][j].delete(0, END)
                matrix[i][j].insert(0, str(value_matrix[i][j]))