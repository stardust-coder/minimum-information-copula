import numpy as np


def load_mic(size, const, mu):
    if const == "rho":
        return np.load("./MIC/result/mics.npy")
    else:
        return np.load("./MIC/result/mick.npy")
