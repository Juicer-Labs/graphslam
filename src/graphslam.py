import numpy as np

def error_func(i, j, z):
    # stachniss' error function
    # return t2v(np.dot(
        # np.inv(z),
        # np.dot(
            # np.inv(v2t(i)),
            # v2t(j)
        # )
    # ))
    # we could also try to compute the  difference: z - (j-i) ??
    return z - (j-i)


def compute_jacobian(v):
    # i think for that error function we just return an identity matrix
    pass


def get_information_matrix(covars):
    result = np.zeros((0,3,3), dtype=np.float32)
    for m in covars:
        result = np.vstack((result, [np.linalg.inv(m)]))

    return result

def graphslam(x, info_matrix, edge_ids, edges):
    n = len(x)*3
    for i in range(10): # 'while not converged'
        print('iteration numba: {}'.format(i))

        b = np.zeros((n), dtype=np.float32)
        H = np.zeros((n, n), dtype=np.float32)
        # for all connected edges
        for e_count, (i, j) in enumerate(edge_ids):
            A_ij = np.identity(3)
            B_ij = -np.identity(3)

            H[i:i+3, i:i+3] += np.dot(A_ij.T, np.dot(info_matrix[i, j], A_ij))
            H[i:i+3, j:j+3] += np.dot(A_ij.T, np.dot(info_matrix[i, j], B_ij))
            H[j:j+3, i:i+3] += np.dot(B_ij.T, np.dot(info_matrix[i, j], A_ij))
            H[j:j+3, j:j+3] += np.dot(B_ij.T, np.dot(info_matrix[i, j], B_ij))

            error = error_func(x[i], x[j], edges[e_count])
            print('error', error)
            print(np.dot(A_ij.T, np.dot(info_matrix[i, j], error)))
            print(A_ij)
            print(A_ij.T)
            b[i:i+3] += np.dot(A_ij.T, np.dot(info_matrix[i, j], error))
            b[j:j+3] += np.dot(B_ij.T, np.dot(info_matrix[i, j], error))

        H[0:3,0:3] += np.identity(3) # Keep first node fixed
        # use sparse solver instead
        delta_x = np.dot(np.linalg.inv(H), -b)
        x += delta_x

    H[0:3,0:3] -= np.identity(3) # Keep first node fixed
    return x, H


