from tkinter import *


class Side:
    def __init__(self, window, title, size, value_matrix, value_number):
        super().__init__()
        self.window = window
        self.title = title
        self.size = size
        self.value_matrix = value_matrix
        self.value_number = value_number
        self.setup()

    def setup(self):
        self.frame = Frame(self.window)
        self.frame.pack(side=LEFT, padx=10, pady=10)

        self.label = Label(self.frame, text=self.title)
        self.label.grid(row=0, columnspan=self.size)

        self.extra_entry = Entry(self.frame)
        self.extra_entry.grid(row=1, columnspan=self.size, sticky="NSEW")

        self.matrix = self.create_matrix()

        self.clear_button = Button(self.frame, text="Очистити",
                                   command=lambda: self.clear_matrix_and_entry())
        self.clear_button.grid(row=6, columnspan=self.size, sticky="NSEW")

        self.predefine_button = Button(self.frame, text=f"Вставити",command=lambda: self.setup_default())
        self.predefine_button.grid(row=7, columnspan=self.size, sticky="NSEW")

        self.predefine_button = Button(self.frame, text=f"Вставити приклад", command=lambda: self.setup_default())
        self.predefine_button.grid(row=8, columnspan=self.size, sticky="NSEW")

        self.copy_button = Button(self.frame, text=f"Копіювати", command=lambda: self.copy_values())
        self.copy_button.grid(row=9, columnspan=self.size, sticky="NSEW")

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

        return f"{self.extra_entry.get()} {matrix}"

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

    def update_size(self, new_size):
        self.frame.destroy()
        self.size = new_size
        self.setup()

    def clear_matrix_and_entry(self):
        self.extra_entry.delete(0, END)
        self.clear_matrix()

    def clear_matrix(self):
        for row in self.matrix:
            for entry in row:
                entry.delete(0, END)

    def clear_matrix_and_entry(self):
        self.extra_entry.delete(0, END)
        self.clear_matrix()

    def setup_default(self):
        self.extra_entry.delete(0, END)
        self.extra_entry.insert(0, str(self.value_number))
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix)):
                self.matrix[i][j].delete(0, END)
                self.matrix[i][j].insert(0, str(self.value_matrix[i][j]))

    def get_converted_as_np(self):
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix)):
                row.append(int(self.matrix[i][j].get()))
            result_matrix.append(row)
        return result_matrix
