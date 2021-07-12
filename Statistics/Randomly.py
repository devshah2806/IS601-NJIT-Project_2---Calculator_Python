import numpy as np


def randoms(r1, r2, r3, r4):
    np.random.seed(r3)
    return np.random.randint(r1, r2, r4)