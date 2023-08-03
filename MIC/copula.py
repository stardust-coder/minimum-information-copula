import numpy as np
from .utils import *
import math
import pandas as pd
import random


epsilon = 1e-7

def example_mick():
    '''
    コードの動作確認用のMICK
    '''
    arr = np.array([[0.06718379, 0.050672  , 0.03708299, 0.02648851, 0.01857271],
       [0.05067187, 0.04743057, 0.04141526, 0.03399389, 0.0264884 ],
       [0.03708292, 0.04141518, 0.04300388, 0.04141519, 0.03708283],
       [0.02648857, 0.03399383, 0.04141511, 0.04743052, 0.05067196],
       [0.01857285, 0.02648841, 0.03708275, 0.05067189, 0.0671841 ]])
    return arr


def plor(tau):
    tb = pd.read_csv("MIC/greedy-mick-30x30.csv")
    ind = tb['tau'].sub(tau).abs().idxmin()
    return tb["pseudo_lor"][ind]

def lor(rho):
    tb = pd.read_csv("MIC/greedy-mics-30x30.csv")
    ind = tb['rho'].sub(rho).abs().idxmin()
    return tb["lor"][ind]


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
   n = size
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
        n = size
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