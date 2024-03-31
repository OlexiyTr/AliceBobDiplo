from fractions import Fraction
from math import lcm
from tkinter import *

import numpy as np


class Calculate:
    def __init__(self):
        super().__init__()
        self.result = []

    def algo(self, result_frame, matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value):
        alice = np.array(matrix_alice.get_converted_as_np())
        bob = np.array(matrix_bob.get_converted_as_np())
        x = np.array(matrix_x.get_converted_as_np())

        alice_inverted = self.inverse_matrix(alice)
        Label(result_frame, text="Обернена матриця Аліси").grid(row=0, column=0, sticky="NSEW")
        self.show_matrix(alice_inverted, result_frame, 1, 0)

        x_by_power_alice = self.power_matrix_by_field_value(x, power_alice, field_value)
        Label(result_frame, text="Матриця Х піднесена до числа Аліси").grid(row=2, column=0, sticky="NSEW")
        self.show_matrix(x_by_power_alice, result_frame, 3, 0)

        bob_inverted = self.inverse_matrix(bob)
        Label(result_frame, text="Обернена матриця Боба").grid(row=0, column=1, sticky="NSEW")
        self.show_matrix(bob_inverted, result_frame, 1, 1)

        x_by_power_bob = self.power_matrix_by_field_value(x, power_bob, field_value)
        Label(result_frame, text="Матриця Х піднесена до числа Боба").grid(row=2, column=1, sticky="NSEW")
        self.show_matrix(x_by_power_bob, result_frame, 3, 1)

        # Alice compute
        alice_computed = np.dot(np.dot(alice, x_by_power_alice), alice_inverted) % field_value
        Label(result_frame, text="Аліса обрахувала T_a*X^a*(T_a^(-1)) і надсилає Бобу").grid(row=4, column=0,
                                                                                             sticky="NSEW")
        self.show_matrix(alice_computed, result_frame, 5, 0)

        # Bob compute
        bob_computed = np.dot(np.dot(bob, x_by_power_bob), bob_inverted) % field_value
        Label(result_frame, text="Боб обрахував T_b*X^b*(T_b^(-1)) і надсилає Алісі").grid(row=4, column=1,
                                                                                           sticky="NSEW")
        self.show_matrix(bob_computed, result_frame, 5, 1)

        print(f"alice computed:{alice_computed}")
        print(f"bob computed:{bob_computed}")

        # Alice power by Bob
        alice_computed_by_power_bob = np.linalg.matrix_power(bob_computed, power_alice) % field_value
        Label(result_frame, text=f"Аліса піднесла отриману матрицю до свого числа {power_alice}").grid(row=6, column=0,
                                                                                                       sticky="NSEW")
        self.show_matrix(alice_computed_by_power_bob, result_frame, 7, 0)

        # Bob power by Alice
        bob_computed_by_power_alice = np.linalg.matrix_power(alice_computed, power_bob) % field_value
        Label(result_frame, text=f"Боб підніс отриману матрицю до свого числа {power_bob}").grid(row=6, column=1,
                                                                                                 sticky="NSEW")
        self.show_matrix(bob_computed_by_power_alice, result_frame, 7, 1)

        print(f"alice compute bobs response power by power_alice:{alice_computed_by_power_bob}")
        print(f"bob compute alice response power by power_bob:{bob_computed_by_power_alice}")

        alice_conjugated = np.dot(np.dot(alice, alice_computed_by_power_bob), alice_inverted) % field_value
        Label(result_frame, text=f"Aліса спрягає результат зі своїм елементом T_a").grid(row=8, column=0,
                                                                                         sticky="NSEW")
        self.show_matrix(alice_conjugated, result_frame, 9, 0)

        bob_conjugated = np.dot(np.dot(bob, bob_computed_by_power_alice), bob_inverted) % field_value
        Label(result_frame, text=f"Боб спрягає результат зі своїм елементом T_b").grid(row=8, column=1,
                                                                                       sticky="NSEW")
        self.show_matrix(bob_conjugated, result_frame, 9, 1)

        print(f"alice conjugated:{alice_conjugated}")
        print(f"bob conjugated:{bob_conjugated}")

    def show_matrix(self, matrix, frame, row_position, column_position):
        matrix_frame = Frame(frame)
        matrix_frame.grid(row=row_position, column=column_position)
        for i in range(len(matrix)):
            row = matrix[i]
            for j in range(len(row)):
                label = (Label(matrix_frame, text=row[j]))
                label.grid(row=i, column=j, sticky="NSEW")

    def power_matrix_by_field_value(self, matrix, power_value, field_value):
        return np.linalg.matrix_power(matrix, power_value) % field_value

    def inverse_matrix(self, matrix):
        return self.to_common_denominator(np.linalg.inv(matrix))

    def to_common_denominator(self, matrix):
        fractions = np.vectorize(Fraction.from_float)(matrix).flatten()
        fractions = [f.limit_denominator() for f in fractions]
        denominators = [f.denominator for f in fractions]
        common_denominator = lcm(*denominators)
        numerators = np.array([f.numerator * (common_denominator // f.denominator) for f in fractions])
        numerators_reshaped = numerators.reshape(matrix.shape)
        return numerators_reshaped
