from tkinter import *
from Column_UI import *
from Processor import calculate_and_display_matrices_sum

window = Tk()
window.title("AliceBob")

matrix_container = Frame(window)
matrix_container.pack(side=TOP, fill=X)

result_frame = Frame(window)
result_frame.pack(side=TOP, fill=X, pady=(10, 0))

frame1, label1, extra_entry1, matrix1 = create_labeled_matrix(matrix_container, "Alice")
frame2, label2, extra_entry2, matrix2 = create_labeled_matrix(matrix_container, "Bob")

buttons_container = Frame(window)
buttons_container.pack(side=TOP, fill=X)

calculate_button = Button(buttons_container, text="Calculate", command=lambda: calculate_and_display_matrices_sum(matrix1, matrix2, result_frame))
calculate_button.pack(side=BOTTOM, fill=X)

window.mainloop()
