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