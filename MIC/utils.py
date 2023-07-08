import numpy as np

eps = 1e-7


def create_Xi(size):
    mat = np.ones(size)*2
    mat = np.tril(mat)
    for i in range(size[0]):
        mat[i][i] = 1
    return mat


def create_uniform(size):
    return np.ones(size)/(size[0]*size[1])


def create_W(size):
    def partial_block(h, w):
        if h == w:
            return np.ones(size)
        elif h > w:
            return create_Xi(size).T
        else:
            return create_Xi(size)

    W = np.block([[partial_block(k, j) for j in range(size[0])]
                 for k in range(size[1])])
    return W


def quad(p1, p2):
    if p1.shape[0] != 1:
        I = p1.shape[0]
        p1 = np.reshape(p1, (1, -1))
    else:
        I = int(p1.shape[1]**0.5)
    if p2.shape[0] != 1:
        J = p2.shape[0]
        p2 = np.reshape(p2, (1, -1))
    else:
        J = int(p2.shape[1]**0.5)

    return np.dot(np.dot(p1, create_W((I, J))), p2.T)


def calc_tau(mat):
    '''
    Should satisfy
    1-quad(mat,mat) = 1-np.trace(np.dot(np.dot(np.dot(B,mat),B),mat.T))
    '''
    B = create_Xi(mat.shape)
    assert abs((1-quad(mat, mat)) -
               (1-np.trace(np.dot(np.dot(np.dot(B, mat), B), mat.T)))) < eps
    return (1-quad(mat, mat)).item()


def calc_rho(mat):
    I = mat.shape[0]
    J = mat.shape[1]
    assert I == J
    summation = 0
    for i in range(I):
        for j in range(J):
            summation += mat[i][j]*(i+1-1/2)*(j+1-1/2)
    return 12*(summation/(I**2)-1/4)


def calc_negentropy(mat):
    res = 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] != 0:
                res += mat[i][j]*np.log(mat[i][j])
    return res



def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    D = (b**2 - 4*a*c) ** (1/2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    if abs(x_1) < 1:
        return x_1
    elif abs(x_2) < 1:
        return x_2
    else:
        print("おかしい")