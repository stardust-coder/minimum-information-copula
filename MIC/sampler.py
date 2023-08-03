import pandas as pd
import random
import numpy as np


def sample_from_ccopula(arr,sample_size, save_csv=False):
    '''
    arr: checkerboard copula in matrix form
    '''
    n = len(arr) #gridsize
    element_list = [i for i in range(n**2)]
    prob_list = list(arr.flatten())
    samples = np.random.choice(element_list,size=sample_size, p=prob_list/sum(prob_list)).tolist()
    count_mat = np.zeros((n,n))
    sampling_data_x,sampling_data_y  = [],[]

    for i in range(n):
        for j in range(n):
            tmp_count = samples.count(n*i+j)
            count_mat[i][j] = tmp_count
            for k in range(tmp_count):
                x = random.uniform(i/n,(i+1)/n)
                y = random.uniform(j/n,(j+1)/n)
                sampling_data_x.append(x)
                sampling_data_y.append(y)        

    df_res = pd.DataFrame()
    df_res["X"] = sampling_data_x
    df_res["Y"] = sampling_data_y

    if save_csv:
        df_res.to_csv(f"output/samples({n}x{n}).csv", index=False)
    return df_res


def MOsamples_clayton(alpha, size):
    def MOsample_clayton(alpha):
        #Laplace変換がgenとなるような分布から1つサンプル
        theta_0 = np.random.gamma(shape=1/alpha, scale=1.0, size=1)
        #一様乱数
        I = np.random.uniform(0, 1, 2)
        #genを作用
        tmp = -(np.log(I)/theta_0)
        U = (tmp + 1)**(-1/alpha)
        return U
    return np.array([MOsample_clayton(alpha) for _ in range(size)])



def MOsamples_gh(gamma, size):
    def MOsample_gh(gamma): #Kanter(1975)
        #Laplace変換がgenとなるような分布から1つサンプル
        v = np.random.uniform()
        w = np.random.exponential()
        theta_0 = ((np.sin((gamma-1)*v/gamma)/w)**(gamma-1))*np.sin(v/gamma)/(np.sin(v)**gamma)
        #一様乱数
        I = np.random.uniform(0, 1, 2)
        #genを作用
        tmp = -(np.log(I)/theta_0)
        U = np.exp(-(tmp)**(1/gamma))
        return U
    return np.array([MOsample_gh(gamma) for _ in range(size)])

def Invsamples_frank(theta,size):
    def Invsample_frank(theta): #Kanter(1975)
        #一様乱数
        I = np.random.uniform(0, 1, 2)
        U1 = I[0]
        U2 = -np.log(1+(I[1]*(1-np.exp(-theta))/(I[1]*(np.exp(-theta*U1)-1)-np.exp(-theta*U1))))/theta
        U = np.array([U1,U2])
        return U
    return np.array([Invsample_frank(theta) for _ in range(size)])
