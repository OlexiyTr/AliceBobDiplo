import numpy as np

# Функція для обчислення оберненої матриці в скінченному полі
def inverse_mod_matrix(matrix, field_size):
    det = int(np.round(np.linalg.det(matrix)))  # Обчислюємо детермінант матриці
    det_inv = pow(det, -1, field_size)  # Обчислюємо обернене число для детермінанта
    matrix_mod_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % field_size
    return matrix_mod_inv

# Функція для піднесення матриці до степеня в скінченому полі
def matrix_power_mod(matrix, power, field_size):
    result = np.eye(matrix.shape[0], dtype=int)  # Одинична матриця
    for _ in range(power):
        result = (np.dot(result, matrix) % field_size).astype(int)
    return result

# Функція для виконання алгоритму некомутативного Діффі-Хеллмана
def non_commutative_diffie_hellman(T, T_prime, X, a, b, field_size):
    # Аліса обчислює (T' * X^b * T^-1)^a
    Alice_computation = matrix_power_mod(
        np.dot(np.dot(T_prime, matrix_power_mod(X, b, field_size)), inverse_mod_matrix(T, field_size)),
        a,
        field_size
    )

    # Боб обчислює (T * X^a * T'^-1)^b
    Bob_computation = matrix_power_mod(
        np.dot(np.dot(T, matrix_power_mod(X, a, field_size)), inverse_mod_matrix(T_prime, field_size)),
        b,
        field_size
    )

    print(f"alice:{Alice_computation}")
    print(f"bob:{Bob_computation}")
    print(f"x:{X}")

    return Alice_computation, Bob_computation

# Приклад ініціалізації матриць та параметрів
T = np.array([[1, 2], [3, 4]])
T_prime = np.array([[4, 3], [2, 1]])
X = np.array([[1, 0], [0, 1]])
a = 3
b = 5
field_size = 7
Alice_computation, Bob_computation = non_commutative_diffie_hellman(T, T_prime, X, a, b, field_size)