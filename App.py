from tkinter import *

from algorithm.CalculateUi import CalculateUi
from model.SideUi import SideUi


class App:
    def __init__(self, size):
        super().__init__()
        self.size = size
        self.calcualte = CalculateUi()

        self.defaults = {
            "2": [[[4, 0], [0, 1]],
                  [[2, 0], [0, 3]],
                  [[5, 0], [0, 7]]],
            "3": [[[1, 0, 3], [1, 0, 1], [1, 2, 1]],
                  [[0, 7, 4], [1, 0, 1], [1, 5, 5]],
                  [[1, 4, 3], [1, 6, 1], [2, 2, 1]]],
            "4": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],
        }

        window = Tk()
        self.window = window
        self.setup_main_tab()
        self.window.mainloop()

    def setup_main_tab(self):
        self.matrix_size = IntVar(value=self.size)
        self.size = self.matrix_size.get()
        self.setup_matrix_frame()
        self.setup_result_frame()
        self.setup_buttons()

    def setup_matrix_frame(self):
        matrix_container = Frame(self.window)
        matrix_container.pack(side=TOP, fill=Y, expand=True)

        self.matrix_x = SideUi(window=matrix_container,
                               title="X",
                               size=self.matrix_size.get(),
                               value_matrix=self.defaults[str(self.matrix_size.get())][0],
                               value_number=0,
                               with_entry=False)

        self.matrix_alice = SideUi(window=matrix_container,
                                   title="Alice",
                                   size=self.matrix_size.get(),
                                   value_matrix=self.defaults[str(self.matrix_size.get())][1],
                                   value_number=2,
                                   with_entry=True)

        self.matrix_bob = SideUi(window=matrix_container,
                                 title="Bob",
                                 size=self.matrix_size.get(),
                                 value_matrix=self.defaults[str(self.matrix_size.get())][2],
                                 value_number=3,
                                 with_entry=True)

    def setup_result_frame(self):
        self.result_frame = Frame(self.window)
        self.result_frame.pack(side=TOP, fill=Y, expand=True)

    def setup_buttons(self):
        Button(self.window, text="Очистити все",
               command=lambda: self.clear_all()).pack(side=BOTTOM, fill=X)

        Button(self.window, text="Обрахувати", command=lambda: self.calculate()).pack(side=BOTTOM, fill=X)

        Label(self.window, text="Скінчене поле над :").pack(side=LEFT)

        self.field_size_entry = Entry(self.window)
        self.field_size_entry.pack(side=LEFT, fill=Y)

        self.create_size_controls()

    def create_size_controls(self):
        size_frame = Frame(self.window)
        size_frame.pack(side=LEFT)

        for size in self.defaults.keys():
            rb = Radiobutton(size_frame, text=f"{size}x{size}", variable=self.matrix_size, value=size,
                             command=self.update_matrices_sizes)
            rb.pack(side=LEFT)

    def update_matrices_sizes(self):
        new_size = self.matrix_size.get()
        self.matrix_x.update_size(new_size, self.defaults[str(self.matrix_size.get())][0])
        self.matrix_alice.update_size(new_size, self.defaults[str(self.matrix_size.get())][1])
        self.matrix_bob.update_size(new_size, self.defaults[str(self.matrix_size.get())][2])

    def clear_all(self):
        self.matrix_alice.clear_matrix_and_entry()
        self.matrix_bob.clear_matrix_and_entry()
        self.matrix_x.clear_matrix()
        for widget in self.result_frame.winfo_children():
            widget.destroy()
        self.field_size_entry.delete(0, END)

    def calculate(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.calcualte.show(
            result_frame=self.result_frame,
            matrix_x=self.matrix_x,
            matrix_alice=self.matrix_alice,
            matrix_bob=self.matrix_bob,
            power_alice=int(self.matrix_alice.extra_entry.get()),
            power_bob=int(self.matrix_bob.extra_entry.get()),
            field_value=int(self.field_size_entry.get()),
        )
