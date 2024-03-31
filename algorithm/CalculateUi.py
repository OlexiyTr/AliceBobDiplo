from tkinter import *
from tkinter.font import Font, BOLD

from algorithm.CalculateAlogithm import CalculateAlgorithm, CalculateResult


class CalculateUi:
    def __init__(self):
        super().__init__()

    def show(self, result_frame, matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value):
        algroithm = CalculateAlgorithm(matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value)
        results = algroithm.calculate()
        alice_result = results[0]
        bob_result = results[1]
        self.show_column(result_frame=result_frame, title="Alice", calculated_result=alice_result, column_position=0)
        self.show_column(result_frame=result_frame, title="Bob", calculated_result=bob_result, column_position=1)

    def show_column(self, result_frame, title, calculated_result: CalculateResult, column_position):
        Label(result_frame, text=title, font=Font(result_frame, size=15, weight=BOLD)).grid(row=0,
                                                                                            column=column_position,
                                                                                            sticky="NSEW")
        self.column_item(
            frame=result_frame,
            title="Обернена матриця",
            matrix=calculated_result.side_matrix_inverted,
            row_position=1,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title=f"Матриця Х піднесена до числа",
            matrix=calculated_result.x_by_power_side_value,
            row_position=2,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title="Обрахована T*X^a*(T^(-1)), яку надішлють співрозмовнику",
            matrix=calculated_result.side_matrix_computed,
            row_position=3,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title="Піднесена отримана матриця до свого числа",
            matrix=calculated_result.another_matrix_powered_by_side_value[0],
            row_position=4,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title="Спряжений результат зі своєю матрицею",
            matrix=calculated_result.side_matrix_conjugated,
            row_position=5,
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
