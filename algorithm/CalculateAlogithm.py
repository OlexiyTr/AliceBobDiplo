import numpy as np

from model.Side import Side


class CalculatedAlgorithm:

    def __init__(self, matrix_alice: Side, matrix_bob: Side, matrix_x: Side, field_value):
        super().__init__()
        self.matrix_alice = matrix_alice
        self.matrix_bob = matrix_bob
        self.matrix_x = matrix_x
        self.field_value = field_value

    def get_results(self):
        alice_matrix = np.array(self.matrix_alice.get_matrix_array())
        bob_matrix = np.array(self.matrix_bob.get_matrix_array())
        x_matrix = np.array(self.matrix_x.get_matrix_array())

        alice_inverted = self.__inverted_matrix(alice_matrix)

        alice_computed = np.dot(np.dot(alice_inverted, x_matrix), alice_matrix) % self.field_value

        bob_inverted = self.__inverted_matrix(bob_matrix)

        bob_computed = np.dot(np.dot(bob_inverted, x_matrix), bob_matrix) % self.field_value

        alice_conjugated = np.dot(np.dot(alice_inverted, bob_computed), alice_matrix) % self.field_value

        bob_conjugated = np.dot(np.dot(bob_inverted, alice_computed), bob_matrix) % self.field_value

        alice_result = CalculatedResult(
            inverted=self.custom_round(alice_inverted),
            computed=self.custom_round(alice_computed),
            conjugated=self.custom_round(alice_conjugated)
        )

        bob_result = CalculatedResult(
            inverted=self.custom_round(bob_inverted),
            computed=self.custom_round(bob_computed),
            conjugated=self.custom_round(bob_conjugated)
        )

        return [alice_result, bob_result]

    def custom_round(self, matrix):
        floor_matrix = np.floor(matrix)
        ceil_matrix = np.ceil(matrix)
        return np.where((matrix - floor_matrix) > 0.5, ceil_matrix, floor_matrix).astype(int)

    def __inverted_matrix(self, matrix):
        determinant = int(np.linalg.det(matrix) % self.field_value)
        inverse = int(self.__mod_inverse(determinant, self.field_value))
        adjugate = self.__matrix_adjugate(matrix)
        result_matrix = np.mod(inverse * adjugate, self.field_value)
        return result_matrix

    def __mod_inverse(self, item, modulo):
        gcd, x, y = self.__extended_gcd(item, modulo)
        if gcd != 1:
            raise Exception('Мультиплікативне обернене не існує')
        else:
            return x % modulo

    def __extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x, y = self.__extended_gcd(b % a, a)
            return gcd, y - (b // a) * x, x

    def __matrix_adjugate(self, matrix):
        if matrix.size == 1:
            return np.array([[1]])

        adjugate_matrix = np.zeros(matrix.shape)

        for row in range(matrix.shape[0]):
            for col in range(matrix.shape[1]):
                adjugate_matrix[row, col] = self.__calc_cofactor(matrix, row, col)
        return adjugate_matrix.T

    def __calc_cofactor(self, matrix, row, col):
        minor = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
        cofactor = ((-1) ** (row + col)) * np.linalg.det(minor)
        return cofactor


class CalculatedResult:
    def __init__(self, inverted, computed, conjugated):
        self.inverted = inverted
        self.computed = computed
        self.conjugated = conjugated
