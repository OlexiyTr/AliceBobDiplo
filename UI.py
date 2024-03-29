from Alogrithm import foo
from Column_UI import *


class Main:
    def __init__(self):
        super().__init__()
        window = Tk()
        window.title("AliceBob")

        size = 2

        matrix_container = Frame(window)
        matrix_container.pack(side=TOP, fill=BOTH, expand=True)

        frame1, label1, matrix1 = create_example_matrix(matrix_container, "X", size, [[1, 0], [0, 1]])

        frame2, label2, extra_entry2, matrix2 = create_labeled_matrix(matrix_container, "Alice", size, [[4, 3], [2, 1]],
                                                                      3)

        frame3, label3, extra_entry3, matrix3 = create_labeled_matrix(matrix_container, "Bob", size, [[1, 2], [3, 4]],
                                                                      5)

        result_frame = Frame(window)
        result_frame.pack(side=TOP, fill=BOTH, expand=True, padx=(5, 0), pady=(5, 0))

        calculate_button = Button(window, text="Calculate",
                                  command=lambda: foo(matrix2, matrix3, matrix1, result_frame, extra_entry2.get(),
                                                      extra_entry3.get(), 7))
        calculate_button.pack(side=BOTTOM, fill=X)

        calculate_button = Button(window, text="Clear all",
                                  command=lambda: clear_all(matrix2, matrix3))
        calculate_button.pack(side=BOTTOM, fill=X)

        window.mainloop()
