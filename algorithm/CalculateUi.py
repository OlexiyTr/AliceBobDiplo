from tkinter import *

from algorithm.CalculateAlogithm import CalculateAlgorithm, CalculateResult


class CalculateUi:
    def __init__(self):
        super().__init__()

    def show(self, result_frame, matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value):
        algroithm = CalculateAlgorithm(matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value)
        results = algroithm.calculate()
        alice_result = results[0]
        bob_result = results[1]
        self.show_column(result_frame=result_frame, title="Аліса", calculated_result=alice_result, column_position=0)
        self.show_column(result_frame=result_frame, title="Боб", calculated_result=bob_result, column_position=1)

    def show_column(self, result_frame, title, calculated_result: CalculateResult, column_position):
        self.column_item(
            frame=result_frame,
            title=f"Обернена матриця {title}",
            matrix=calculated_result.side_matrix_inverted,
            label_row_position=0,
            matrix_row_position=1,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title=f"Матриця Х піднесена до числа {title}",
            matrix=calculated_result.x_by_power_side_value,
            label_row_position=2,
            matrix_row_position=3,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title=f"{title} обрахував T*X^a*(T^(-1)) і надсилає співрозмовнику",
            matrix=calculated_result.side_matrix_computed,
            label_row_position=4,
            matrix_row_position=5,
            column_position=column_position,
        )

        print(calculated_result.side_matrix_computed)
        print(calculated_result.another_matrix_powered_by_side_value)

        self.column_item(
            frame=result_frame,
            title=f"{title} піднесла отриману матрицю до свого числа",
            matrix=calculated_result.another_matrix_powered_by_side_value,
            label_row_position=6,
            matrix_row_position=7,
            column_position=column_position,
        )

        self.column_item(
            frame=result_frame,
            title=f"{title} спрягає результат зі своїм елементом T_a",
            matrix=calculated_result.side_matrix_conjugated,
            label_row_position=8,
            matrix_row_position=9,
            column_position=column_position,
        )

    def column_item(self, frame, title, matrix, label_row_position, matrix_row_position, column_position):
        Label(frame, text=title).grid(row=label_row_position,
                                      column=column_position,
                                      sticky="NSEW")
        self.show_matrix(
            matrix=matrix,
            frame=frame,
            row_position=matrix_row_position,
            column_position=column_position)

    def show_matrix(self, matrix, frame, row_position, column_position):
        matrix_frame = Frame(frame)
        matrix_frame.grid(row=row_position, column=column_position)
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                label = (Label(matrix_frame, text=row[j]))
                label.grid(row=i, column=j, sticky="NSEW")
