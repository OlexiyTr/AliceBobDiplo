from tkinter import *

from model.Side import Side
from model.Side_X import Side_X


class App:
    def __init__(self, size):
        super().__init__()
        window = Tk()
        self.matrix_size = IntVar(value=size)
        self.size = size

        matrix_container = Frame(window)
        matrix_container.pack(side=TOP, fill=Y, expand=True)

        self.matrix_x = Side_X(matrix_container, "X", self.size, [[1, 0], [0, 1]])
        self.matrix_alice = Side(matrix_container, "Alice", self.size, [[4, 3], [2, 1]], value_number=3)
        self.matrix_bob = Side(matrix_container, "Bob", self.size, [[1, 4], [1, 3]], value_number=1)

        self.result_frame = Frame(window)
        self.result_frame.pack(side=TOP, fill=BOTH, expand=True, padx=(5, 0), pady=(5, 0))

        self.calculate_button = Button(window, text="Calculate")
        self.calculate_button.pack(side=BOTTOM, fill=X)

        self.calculate_button = Button(window, text="Clear all",
                                       command=lambda: self.clear_all())
        self.calculate_button.pack(side=BOTTOM, fill=X)

        self.create_size_controls(window)

        window.mainloop()

    def create_size_controls(self, window):
        size_frame = Frame(window)
        size_frame.pack(side=BOTTOM)

        for idx, size in enumerate([2, 3, 4]):
            rb = Radiobutton(size_frame, text=f"{size}x{size}", variable=self.matrix_size, value=size,
                             command=self.update_matrices_sizes)
            rb.pack(side=LEFT)

    def update_matrices_sizes(self):
        new_size = self.matrix_size.get()
        self.matrix_x.update_size(new_size)
        self.matrix_alice.update_size(new_size)
        self.matrix_bob.update_size(new_size)

    def clear_all(self):
        self.matrix_alice.clear_matrix_and_entry()
        self.matrix_bob.clear_matrix_and_entry()
        self.matrix_x.clear_matrix()
