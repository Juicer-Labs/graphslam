import numpy as np

class Edge:
    def __init__(self, ids, estimate, infoMatrix, invertInfo = True):
        self.ids = ids # (id1, id2)
        self.estimate = estimate # dx dy dth
        # 3x3 info matrix
        self.infoMatrix = np.array(infoMatrix, dtype=np.float32)
        if invertInfo: # Inverto info in case a covar matrix was provided
            self.infoMatrix = np.linalg.inv(self.infoMatrix)

    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def calc_jacobians(self):
        pass


