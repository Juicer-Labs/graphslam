import numpy as np
import matplotlib.pyplot as plt


class Edge:

    def __init__(self, ids, estimate, info_matrix, invert_info=True):
        self.ids = ids  # (id1, id2)
        self.estimate = estimate  # dx, dy, dth
        self.info_matrix = np.array(info_matrix, dtype=np.float32)  # 3x3 info matrix

        # Invert information matrix in case a covariance matrix was provided.
        if invert_info:
            self.info_matrix = np.linalg.inv(self.info_matrix)

    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def calc_jacobians(self):
        pass

    def plot(self, vertices):
        x1s = []; y1s = []; x2s = []; y2s = []
        
        id1, id2 = self.ids
        x1, y1, _ = vertices[id1]
        x2, y2, _ = vertices[id2]
        plt.plot(x1s, y1s, x2s, y2s, marker='', color='green', zorder=0)


