from tkinter import *
from tkinter.ttk import Notebook

from algorithm.Calculate import Calculate
from model.Side import Side
from model.Side_X import Side_X


class App:
    def __init__(self, size):
        super().__init__()

        self.size = size
        self.calcualte = Calculate()
        #self.history = []
        self.defaults = {
            "2": [[[1, 0], [0, 1]],
                  [[1, 2], [3, 4]],
                  [[3, 2], [5, 4]]],
            "3": [[[1, 0, 3], [1, 0, 1], [1, 2, 1]],
                  [[0, 7, 4], [1, 0, 1], [1, 5, 5]],
                  [[1, 4, 3], [1, 6, 1], [2, 2, 1]]],
            "4": [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                  [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]],
        }

        window = Tk()

        self.setup_tabs(window)
        self.setup_main_tab()
        window.mainloop()

    def setup_tabs(self, window):
        self.tabControl = Notebook(window)
        self.tab_main = Frame(self.tabControl)
        self.tab_history = Frame(self.tabControl)
        self.tabControl.add(self.tab_main, text='Main')
        self.tabControl.add(self.tab_history, text='History')
        self.tabControl.pack(expand=True, fill=X)

    def setup_main_tab(self):
        self.matrix_size = IntVar(value=self.size)
        self.size = self.matrix_size.get()
        matrix_container = Frame(self.tab_main)
        matrix_container.pack(side=TOP, fill=Y, expand=True)

        self.matrix_x = Side_X(matrix_container, "X", self.size, self.defaults[str(self.matrix_size.get())][0])

        self.matrix_alice = Side(window=matrix_container,
                                 title="Alice",
                                 size=self.size,
                                 value_matrix=self.defaults[str(self.matrix_size.get())][1],
                                 value_number=3)

        self.matrix_bob = Side(window=matrix_container,
                               title="Bob",
                               size=self.size,
                               value_matrix=self.defaults[str(self.matrix_size.get())][2],
                               value_number=1)

        self.result_frame = Frame(self.tab_main)
        self.result_frame.pack(side=TOP, fill=BOTH, expand=True, padx=(5, 0), pady=(5, 0))

        self.calculate_button = Button(self.tab_main, text="Обрахувати", command=lambda: self.calculate())
        self.calculate_button.pack(side=BOTTOM, fill=X)

        self.clear_all_button = Button(self.tab_main, text="Почистити все",
                                       command=lambda: self.clear_all())
        self.clear_all_button.pack(side=BOTTOM, fill=X)
        self.create_size_controls()

    def create_size_controls(self):
        size_frame = Frame(self.tab_main)
        size_frame.pack(side=BOTTOM)

        for size in self.defaults.keys():
            rb = Radiobutton(size_frame, text=f"{size}x{size}", variable=self.matrix_size, value=size,
                             command=self.update_matrices_sizes)
            rb.pack(side=LEFT)

    def update_matrices_sizes(self):
        new_size = self.matrix_size.get()

        self.matrix_x.update_size(new_size,self.defaults[str(self.matrix_size.get())][0])
        self.matrix_alice.update_size(new_size, self.defaults[str(self.matrix_size.get())][1])
        self.matrix_bob.update_size(new_size, self.defaults[str(self.matrix_size.get())][2])

    def clear_all(self):
        self.matrix_alice.clear_matrix_and_entry()
        self.matrix_bob.clear_matrix_and_entry()
        self.matrix_x.clear_matrix()

    def calculate(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()

        self.calcualte.invoke(self.matrix_alice, self.matrix_bob, self.result_frame)
        #self.history.append(self.calcualte.result)
