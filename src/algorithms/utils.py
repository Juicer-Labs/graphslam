import numpy as np

def v2t((x,y,yaw)):
    """Vector (SE2) to transformation"""
    return np.array(
        [
            [np.cos(yaw), -np.sin(yaw), x],
            [np.sin(yaw),  np.cos(yaw), y],
            [0, 0, 1],
        ]
    )

def t2v(t):
    """Transformation to Vector (SE2)"""

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
