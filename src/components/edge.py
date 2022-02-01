import numpy as np
import matplotlib.pyplot as plt


class Edge(object):

    def __init__(self, ids, estimate, info_matrix, invert_info=True):
        self.ids = ids  # (id1, id2)
        self.estimate = estimate  # (dx, dy, dth)
        self.info_matrix = info_matrix  # 3x3 information matrix

        # Invert information matrix in case a covariance matrix was provided.
        if invert_info:
            self.info_matrix = np.linalg.inv(self.info_matrix)

    #############
    ### MATHS ###
    #############
    
    def calc_error(self, vertices):
        err = self.estimate - (vertices[self.ids[1]] - vertices[self.ids[0]])
        return np.dot(np.transpose(err), np.dot(self.info_matrix,  err))

    def calc_error_gradient_hessian(self):
        grad = {
            v.index: np.dot(np.dot(np.transpose(err), self.information), jacobian) for v, jacobian in zip(self.vertices, jacobians)
        }


        h = {(self.vertices[i].index, self.vertices[j].index): np.dot(np.dot(np.transpose(jacobians[i]), self.information), jacobians[j]) for i in range(len(jacobians)) for j in range(i, len(jacobians))}

    def calc_jacobians(self):
        jacobian = np.zeros((3,3))

    ###############
    ### DUNDERS ###
    ###############

    def __repr__(self):
        return "Edge: {}, {}, {}".format(self.ids, self.estimate, self.info_matrix)

    def __str__(self):
        return "Edge: {}, {}, {}".format(self.ids, self.estimate, self.info_matrix)

