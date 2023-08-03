import numpy as np
from .utils import *
import math
import pandas as pd
import random

epsilon = 1e-7

def load_mic(size, const, mu):
    if const == "rho":
        return np.load("MIC/result/mics.npy")
    else:
        return np.load("MIC/result/mick.npy")

def greedy_mic(size,const,inv):
    '''
    inv: (pseudo) log odds ratio
    '''
    def solve_movement_MICK(theta,x1,x2,x3,x4):
        a = 1-math.exp(theta*(x1+x2+x3+x4))
        b = x1+x4+(x2+x3)*math.exp(theta*(x1+x2+x3+x4))
        c = x1*x4 - x2*x3*math.exp(theta*(x1+x2+x3+x4))
        solution = solv_quadratic_equation(a,b,c)
        return solution

    def solve_movement_MICS(theta,x1,x2,x3,x4):
        a = 1-math.exp(theta)
        b = x1+x4+(x2+x3)*math.exp(theta)
        c = x1*x4 - x2*x3*math.exp(theta)
        solution = solv_quadratic_equation(a,b,c)
        return solution

    def greedy_MICK(size,invariance):
        n = size #n=30で45s.
        opt = create_uniform((n,n))

        while True: 
            max_delta = 0
            for i in range(n-1):
                for j in range(n-1):
                    delta = solve_movement_MICK(invariance,opt[i][j],opt[i+1][j],opt[i][j+1],opt[i+1][j+1])
                    opt[i][j] += delta
                    opt[i+1][j+1] += delta
                    opt[i+1][j] -= delta
                    opt[i][j+1] -= delta
                    if delta > max_delta:
                        max_delta = delta
            if abs(max_delta) < epsilon:
                break
        return opt
    
    def greedy_MICS(size,invariance):
        n = size #n=30で45s.
        opt = create_uniform((n,n))

        while True: 
            max_delta = 0
            for i in range(n-1):
                for j in range(n-1):
                    delta = solve_movement_MICS(invariance,opt[i][j],opt[i+1][j],opt[i][j+1],opt[i+1][j+1])
                    opt[i][j] += delta
                    opt[i+1][j+1] += delta
                    opt[i+1][j] -= delta
                    opt[i][j+1] -= delta
                    if delta > max_delta:
                        max_delta = delta
            if abs(max_delta) < epsilon:
                break
        return opt
    
    if const=="rho":
        return greedy_MICS(size,inv)
    else:
        return greedy_MICK(size,inv)
    

