from tkinter import *


class Side:
    def __init__(self, window, title, size, value_matrix):
        super().__init__()
        self.window = window
        self.title = title
        self.size = size
        self.value_matrix = value_matrix
        self.setup()

    def setup(self):
        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT, padx=10, pady=10)

        self.label = Label(self.frame, text=self.title)
        self.label.grid(row=0, columnspan=self.size)

        self.matrix = self.create_matrix()
        self.setup_buttons_frame()
        self.setup_methods_frame()

    def setup_buttons_frame(self):
        self.buttons_frame = Frame(self.frame)
        self.buttons_frame.grid(row=6, columnspan=self.size, sticky="NSEW")

        self.buffer_button = Button(self.buttons_frame, text=f"Вставити з буферу",
                                    command=lambda: self.setup_from_buffer())
        self.buffer_button.grid(row=0, column=0, sticky="NSEW")

        self.example_button = Button(self.buttons_frame, text=f"Вставити приклад", command=lambda: self.setup_default())
        self.example_button.grid(row=0, column=1, sticky="NSEW")

        self.buffer_example_label = Label(self.buttons_frame, text=f"Формат прикладу буферу:'{self.value_matrix}'")
        self.buffer_example_label.grid(row=1, columnspan=self.size, sticky="NSEW")

        self.buttons_frame.columnconfigure(0, weight=1)
        self.buttons_frame.columnconfigure(1, weight=1)

    def setup_methods_frame(self):
        self.methods_frame = Frame(self.frame)
        self.methods_frame.grid(row=7, columnspan=self.size, sticky="NSEW")

        self.clear_button = Button(self.methods_frame, text="Очистити",
                                   command=lambda: self.clear_matrix_and_entry())
        self.clear_button.grid(row=0, column=0, sticky="NSEW")

        self.copy_button = Button(self.methods_frame, text=f"Копіювати", command=lambda: self.copy_values())
        self.copy_button.grid(row=0, column=1, sticky="NSEW")

        self.methods_frame.columnconfigure(0, weight=1)
        self.methods_frame.columnconfigure(1, weight=1)

    def copy_values(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.convert_to_string())

    def convert_to_string(self):
        matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix)):
                row.append(int(self.matrix[i][j].get()))
            matrix.append(row)
        return f"{matrix}"

    def create_matrix(self):
        matrix = []
        for i in range(self.size):
            row = []
            for j in range(self.size):
                entry = Entry(self.frame, width=5)
                entry.grid(row=i + 2, column=j, sticky="NSEW")
                row.append(entry)
            matrix.append(row)
        return matrix

    def update_size(self, new_size, value_matrix):
        self.frame.destroy()
        self.size = new_size
        self.value_matrix = value_matrix
        self.setup()

    def clear_matrix(self):
        for row in self.matrix:
            for entry in row:
                entry.delete(0, END)

    def clear_matrix_and_entry(self):
        self.clear_matrix()

    def setup_default(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].delete(0, END)
                self.matrix[i][j].insert(0, str(self.value_matrix[i][j]))

    def setup_from_buffer(self):
        matrix = self.parse_matrix(self.window.clipboard_get())
        print(matrix)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                self.matrix[i][j].delete(0, END)
                self.matrix[i][j].insert(0, str(matrix[i][j]))

    def parse_matrix(self, matrix_string):
        rows = matrix_string.strip("[]").split("], [")
        matrix = [list(map(int, row.split(", "))) for row in rows]
        return matrix

    def get_matrix_array(self):
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix)):
                row.append(int(self.matrix[i][j].get()))
            result_matrix.append(row)
        return result_matrix
