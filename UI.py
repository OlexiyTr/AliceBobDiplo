from tkinter import *
from Column_UI import *
from Processor import calculate_matrices_sum

# Створення вікна Tkinter
window = Tk()
window.title("Операції з матрицями")

# Створення контейнера для матриць
matrix_container = Frame(window)
matrix_container.pack(side=TOP, fill=X)

frame1, label1, extra_entry1, matrix1 = create_labeled_matrix(matrix_container, "Alice")
frame2, label2, extra_entry2, matrix2 = create_labeled_matrix(matrix_container, "Bob")

# Створення фрейму для відображення результату в тому ж matrix_container
result_frame = Frame(matrix_container)
result_frame.pack(side=LEFT, padx=10, pady=10)

# Додавання загальної кнопки під контейнером з матрицями, яка викликає функцію обрахунку
calculate_button = Button(window, text="Calculate",
                          command=lambda: calculate_matrices_sum(matrix1, matrix2, result_frame))
calculate_button.pack(side=BOTTOM, fill=X)

window.mainloop()
