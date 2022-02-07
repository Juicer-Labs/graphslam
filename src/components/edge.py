import numpy as np
import matplotlib.pyplot as plt

from transformation_funcs import v2t, t2v, inv_trans


class Edge(object):

    def __init__(self, ids, estimate, info_matrix, invert_info=False):
        self.ids = ids  # (id1, id2)
        self.estimate = estimate  # (dx, dy, dth)
        self.transformation_estimate = v2t(estimate)
        self.info_matrix = info_matrix  # 3x3 information matrix

        # Invert information matrix in case a covariance matrix was provided.
        if invert_info:
            self.info_matrix = np.linalg.inv(self.info_matrix)

    #############
    ### MATHS ###
    #############

    def calc_error(self, i, j):
        """
        Calculates error between two SE2 pose vertices
        Params:
            i, j: graph pose vertices - (x,y,yaw)
        Formula:
            t2v(Z^-1 * (Xi^-1 * Xj))
            where Z, Xi, Xj are transformation matrices
        """

        return t2v(
            np.dot(
                inv_trans(v2t(self.estimate)),
                np.dot(inv_trans(v2t(i)), v2t(j))
            )
        )

    def calc_jacobians(self, i, j):
        """
        Returns 3x3 matrices A,B - jacobian of error function with respect to edges i,j
        Pose to Pose
        """

        """
        # NOTE(gonk): there are possible optimisations to be done here
        Xi = v2t(i)
        Xj = v2t(j)

        # Rotations
        Xi_R_T = Xi[0:2, 0:2].T
        Zij_R_T = self.transformation_estimate[0:2,0:2].T

        # Compute derivative of rotational element of i with respect to theta 
        st = -np.sin(i[2]) # sin of th
        ct = np.cos(i[2]) # cos of th
        dRi_dTh_T = np.array([[st, ct], [-ct, st]]) # Already transposed

        A = np.zeros((3,3))
        A[0:2, 0:2] = -np.dot(Zij_R_T, Xi_R_T)
        A[0:2, 2] = np.dot(Zij_R_T, np.dot(dRi_dTh_T, (j[0:2] - i[0:2])))
        A[2,2] = -1

        B = np.zeros((3,3))
        B[0:2, 0:2] = np.dot(Zij_R_T, Xi_R_T)
        B[2,2] = 1

        return A,B
        """

        # Debug
        zt_ij = v2t(self.estimate)
        vt_i = v2t(i)
        vt_j = v2t(j)

        R_i = vt_i[0:2, 0:2]
        R_ij = zt_ij[0:2, 0:2]
        ct_i = np.cos(i[2])
        st_i = np.sin(i[2])
        dRdT_i = np.array([[-st_i, ct_i], [-ct_i, -st_i]])

        e = t2v(np.dot(inv_trans(zt_ij), np.dot(inv_trans(vt_i), vt_j)))
        A = np.zeros((3,3))
        A[0:2,0:2] = np.dot(-R_ij.T, R_i.T)
        A[0:2, 2] = np.dot(R_ij.T, np.dot(dRdT_i, j[0:2]-i[0:2]))
        A[2,2] = -1

        B = np.zeros((3,3))
        B[0:2, 0:2] = np.dot(R_ij.T, R_i.T)
        B[2,2] = 1

        return e,A,B


    ###############
    ### DUNDERS ###
    ###############

    def __repr__(self):
        return ("Edge: {}, {}, {}").format(self.ids, self.estimate, self.info_matrix)

    def __str__(self):
        return ("Edge: {}, {}, {}").format(self.ids, self.estimate, self.info_matrix)

