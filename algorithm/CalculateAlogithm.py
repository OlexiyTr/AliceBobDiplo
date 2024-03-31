from fractions import Fraction
from math import lcm

import numpy as np


class CalculateAlgorithm:

    def __init__(self, matrix_alice, matrix_bob, matrix_x, power_alice, power_bob, field_value):
        super().__init__()
        self.matrix_alice = matrix_alice
        self.matrix_bob = matrix_bob
        self.matrix_x = matrix_x
        self.power_alice = power_alice
        self.power_bob = power_bob
        self.field_value = field_value

    def calculate(self):
        alice_matrix = np.array(self.matrix_alice.get_converted_as_np())
        bob_matrix = np.array(self.matrix_bob.get_converted_as_np())
        x_matrix = np.array(self.matrix_x.get_converted_as_np())

        alice_inverted = self.__inverse_matrix(alice_matrix)
        x_by_power_alice = np.linalg.matrix_power(x_matrix, self.power_alice) % self.field_value

        bob_inverted = self.__inverse_matrix(bob_matrix)
        x_by_power_bob = np.linalg.matrix_power(x_matrix, self.power_bob) % self.field_value

        alice_computed = np.dot(np.dot(alice_matrix, x_by_power_alice), alice_inverted) % self.field_value
        bob_computed = np.dot(np.dot(bob_matrix, x_by_power_bob), bob_inverted) % self.field_value

        bob_computed_by_alice_power = np.linalg.matrix_power(bob_computed, self.power_alice) % self.field_value

        alice_computed_by_bob_power = np.linalg.matrix_power(alice_computed, self.power_bob) % self.field_value

        alice_conjugated = np.dot(np.dot(alice_matrix, bob_computed_by_alice_power), alice_inverted) % self.field_value
        bob_conjugated = np.dot(np.dot(bob_matrix, alice_computed_by_bob_power), bob_inverted) % self.field_value

        alice_result = CalculateResult(
            side_matrix_inverted=alice_inverted,
            x_by_power_side_value=x_by_power_alice,
            side_matrix_computed=alice_computed,
            another_matrix_powered_by_side_value=bob_computed_by_alice_power,
            side_matrix_conjugated=alice_conjugated
        )

        bob_result = CalculateResult(
            side_matrix_inverted=bob_inverted,
            x_by_power_side_value=x_by_power_bob,
            side_matrix_computed=bob_computed,
            another_matrix_powered_by_side_value=alice_computed_by_bob_power,
            side_matrix_conjugated=bob_conjugated
        )

        return [alice_result, bob_result]

    def __inverse_matrix(self, matrix):
        return self.__to_common_denominator(np.linalg.inv(matrix))

    def __to_common_denominator(self, matrix):
        fractions = np.vectorize(Fraction.from_float)(matrix).flatten()
        fractions = [f.limit_denominator() for f in fractions]
        denominators = [f.denominator for f in fractions]
        common_denominator = lcm(*denominators)
        numerators = np.array([f.numerator * (common_denominator // f.denominator) for f in fractions])
        numerators_reshaped = numerators.reshape(matrix.shape)
        return numerators_reshaped


class CalculateResult:
    def __init__(self,
                 side_matrix_inverted,
                 x_by_power_side_value,
                 side_matrix_computed,
                 another_matrix_powered_by_side_value,
                 side_matrix_conjugated):
        self.side_matrix_inverted = side_matrix_inverted
        self.x_by_power_side_value = x_by_power_side_value
        self.side_matrix_computed = side_matrix_computed
        self.another_matrix_powered_by_side_value = another_matrix_powered_by_side_value,
        self.side_matrix_conjugated = side_matrix_conjugated
