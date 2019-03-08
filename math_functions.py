import numpy as np
import math
from diophantine import *
import logging



def rounding(x, isInt):
    """Returns the componentwise rounding x_check of some point x (list or numpy array),
       where x_check[i] = x[i], if isInt is false, and x_check[i] = round(x[i]), otherwise """
    x = np.array(x)
    x_check = np.array(x)
    x_check[isInt] = np.round(x[isInt])
    return x_check


def floor_g(a, g):
    result = a
    if g != 0:
        result = math.floor(a) - (math.floor(a) % g)
        if (a-result) >= g -1e-6:
            logging.warning("A righthandside may be unvoluntarily rounded. Confirm!")
    return result


def gcd_vec(a):
    a = np.array(a)
    a_nz = a[np.nonzero(a)]
    if (any(a_nz == 1)):
        result = 1
    else:
        result = int(a_nz[0])
        for i in a[1:]:
            result = math.gcd(result, int(i))
            if result == 1:
                break
    return result

def comp_sol_space(D, gamma):
    print(D.shape)
    H, U, rank = lllhermite(Matrix(D.transpose()))
    H = H.transpose()
    U = U.transpose()
    K = H[:, :rank]
    U1 = U[:, :rank]
    U2 = U[:, rank:]
    gamma = Matrix(gamma)
    const_vec = U1 * K.inv() * gamma
    subst_matrix = U2
    return const_vec, subst_matrix
