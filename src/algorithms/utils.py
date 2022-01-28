import numpy as np


def calculate_covariance(matrix):
    result = np.cov(matrix)
    return result


def calculate_information(matrix):
    pass


def compute_jacobians(matrix):
    A, B = None, None


if __name__ == "__main__":

    matrix = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    cov_matrix = calculate_covariance(matrix)