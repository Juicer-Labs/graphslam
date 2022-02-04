import numpy as np


def v2t(i):
    """
    Transforms SE2 pose (x,y,yaw) into 3x3 homogeneous transformation matrix
    """

    ct = np.cos(i[2])
    st = np.sin(i[2])

    return np.array([
        [ct, -st, i[0]],
        [st,  ct, i[1]],
        [ 0,   0,   1]]
    )


def t2v(m):
    """
    Transforms 3x3 homogeneous transformation matrix into SE2 pose (x,y,yaw)
    """

    return np.array([
        m[0, 2],
        m[1, 2],
        np.arctan2(m[0,1], m[1,1]) # atan(sinx/cosx) = atan(tanx) = x
    ])


def inv_trans(m):
    """
    Returns inverse of 3x3 homogeneous transformation matrix
    [R.T, -R.T*t]
    [  0,    1  ]
        where R is the rotational component of m
        where t is the translation component of m
    """

    RT = m[0:2, 0:2].T
    trans = m[0:2, 2]
    result = np.zeros((3,3))
    result[0:2, 0:2] = RT
    result[2,2] = 1
    result[0:2, 2] = -np.dot(RT, trans)

    return result
