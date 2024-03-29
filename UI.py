from tkinter import *
from Column_UI import *
from Processor import calculate_matrices_sum

window = Tk()
window.title("Операції з матрицями")

matrix_container = Frame(window)
matrix_container.pack(side=TOP, fill=BOTH, expand=True)

frame1, label1, matrix1 = create_example_matrix(matrix_container, "X")

frame2, label2, extra_entry2, matrix2 = create_labeled_matrix(matrix_container, "Alice")

frame3, label3, extra_entry3, matrix3 = create_labeled_matrix(matrix_container, "Bob")

result_frame = Frame(window)
result_frame.pack(side=TOP, fill=BOTH, expand=True, pady=(5, 0))

calculate_button = Button(window, text="Calculate", command=lambda: calculate_matrices_sum(matrix2, matrix3, result_frame))
calculate_button.pack(side=BOTTOM, fill=X)

calculate_button = Button(window, text="Clear all")
calculate_button.pack(side=BOTTOM, fill=X)

window.mainloop()
