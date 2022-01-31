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
    n = len(x)
    for i in range(10): # 'while not converged'
        print('iteration numba: {}'.format(i))

        b = np.zeros((n, 3), dtype=np.float32)
        H = np.zeros((n, n, 3,3), dtype=np.float32)
        # for all connected edges
        for e_count, (i, j) in enumerate(edge_ids):
            A_ij = np.identity(3)
            B_ij = -np.identity(3)

            # H[i:i+3, i:i+3] += np.dot(A_ij.T, np.dot(info_matrix[e_count], A_ij))
            # H[i:i+3, j:j+3] += np.dot(A_ij.T, np.dot(info_matrix[e_count], B_ij))
            # H[j:j+3, i:i+3] += np.dot(B_ij.T, np.dot(info_matrix[e_count], A_ij))
            # H[j:j+3, j:j+3] += np.dot(B_ij.T, np.dot(info_matrix[e_count], B_ij))
            H[i, i] += np.dot(A_ij.T, np.dot(info_matrix[e_count], A_ij))
            H[i, j] += np.dot(A_ij.T, np.dot(info_matrix[e_count], B_ij))
            H[j, i] += np.dot(B_ij.T, np.dot(info_matrix[e_count], A_ij))
            H[j, j] += np.dot(B_ij.T, np.dot(info_matrix[e_count], B_ij))

            error = error_func(x[i], x[j], edges[e_count])

            # print '\nerror', error
            # print '\nresult\n', np.dot(A_ij.T, np.dot(info_matrix[e_count], error))
            # print('\nA_ij\n', A_ij)
            # print('\nA_ij.T\n', A_ij.T)
            # print '\nb\n', b

            # print 'info x error'
            # print np.dot(info_matrix[e_count], error)
            # print 'info mat'
            # print info_matrix[e_count]

            # print 'info mat length ' + str(len(info_matrix)) + ' n= ' + str(n)
            # print 'cum'
            # print info_matrix[e_count]

            b[i] += np.dot(A_ij.T, np.dot(info_matrix[e_count], error))
            b[j] += np.dot(B_ij.T, np.dot(info_matrix[e_count], error))

        print 'cum'
        print H[0,0]
        H[0,0] += np.identity(3) # Keep first node fixed
        print H[0,0]
        # print 'det of H: ' + str(np.linalg.det(H.reshape(n*3, n*3)))
        # print 'shape of H: ' + str(H.reshape(n*3, n*3).shape)
        # use sparse solver instead
        delta_x = np.dot(np.linalg.inv(H.reshape(n*3, n*3)), -b)
        x += delta_x

    H[0,0] -= np.identity(3) # Keep first node fixed
    return x, H


