import numpy as np


def calculate_covariance(matrix):
    result = np.cov(matrix)
    return result


if __name__ == "__main__":

    matrix = [
        [1, 2, 3],
        [1, 2, 3],
        [1, 2, 3]
    ]

    print(calculate_covariance(matrix))