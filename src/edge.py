import numpy as np

class Edge:

    def __init__(self, ids, estimate, info_matrix, invert_info=True):
        self.ids = ids # (id1, id2)
        self.estimate = estimate # dx, dy, dth
        # 3x3 info matrix
        self.info_matrix = np.array(infoMatrix, dtype=np.float32)

        # Invert info in case a covariance matrix was provided
        if invert_info:
            self.info_matrix = np.linalg.inv(self.info_matrix)

    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def calc_jacobians(self):
        pass


