from tkinter import *
from tkinter.font import Font, BOLD

from algorithm.CalculateAlogithm import CalculatedAlgorithm, CalculatedResult


class CalculateUi:
    def __init__(self):
        super().__init__()

    def show(self, result_frame, matrix_alice, matrix_bob, matrix_x, field_value):
        algroithm = CalculatedAlgorithm(matrix_alice, matrix_bob, matrix_x, field_value)
        results = algroithm.get_results()
        alice_result = results[0]
        bob_result = results[1]
        self.show_column(result_frame=result_frame, title="Alice", calculated_result=alice_result, column_position=0)
        self.show_column(result_frame=result_frame, title="Bob", calculated_result=bob_result, column_position=1)

    def show_column(self, result_frame, title, calculated_result: CalculatedResult, column_position):
        Label(result_frame, text=title, font=Font(result_frame, size=15, weight=BOLD)).grid(row=0,
                                                                                            column=column_position,
                                                                                            sticky="NSEW")
        self.column_item(
            frame=result_frame,
            title="Обернена матриця",
            matrix=calculated_result.inverted,
            row_position=1,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title="Обрахована матриця T^(-1)*X*T",
            matrix=calculated_result.computed,
            row_position=2,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title="Спряжений результат зі своєю матрицею",
            matrix=calculated_result.conjugated,
            row_position=3,
            column_position=column_position,
        )

    def column_item(self, frame, title, matrix, row_position, column_position):
        column_item_frame = Frame(frame)
        column_item_frame.grid(row=row_position, column=column_position)
        Label(column_item_frame, text=title).grid(
            row=0,
            column=column_position,
            sticky="NSEW"
        )
        self.show_matrix(
            matrix=matrix,
            frame=column_item_frame,
            row_position=1,
            column_position=column_position)

    def show_matrix(self, matrix, frame, row_position, column_position):
        matrix_frame = Frame(frame)
        matrix_frame.grid(row=row_position, column=column_position)
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                label = (Label(matrix_frame, text=row[j]))
                label.grid(row=i, column=j, sticky="NSEW")
