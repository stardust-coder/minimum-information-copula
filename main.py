from MIC import *
from MIC.utils import *
from MIC.visualize import *
from MIC.calc import *

import sys
import argparse


def get_args():
    # 準備
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", help="optional", type=str)
    parser.add_argument("--mode", help="how to obtain MIC", default='greedy')

    # 結果を受ける
    args = parser.parse_args()

    return args

def run_from_load():
    '''
    data: Pandas.DataFrame
    '''
    mat = load_mic(size=(30, 30), const="tau", mu=0.5)
    fig = three_dim_plot_flatten(mat, bottom=0, top=0.1)
    np.save("result/temp", mat)
    plt.savefig("result/temp.png")


def plot(size,const,mu,mode):
    if mode == "greedy":
        inv = 10
        mat = greedy_mic(size,"tau",inv)
    elif mode == "load":
        mat = load_mic(size=(30, 30), const="tau", mu=0.5)
    else:
        mat = load_mic(size=(30, 30), const="tau", mu=0.5) #optimize by scipy
    fig = three_dim_plot_flatten(mat, bottom=0, top=1/size)
    np.save("result/temp", mat)
    plt.savefig("result/temp.png")

def run():
    '''
    data: Pandas.DataFrame
    mode: optim, greedy, load
    '''
    args = get_args()
    print(args.data)
    print(args.mode)

    mat = load_mic(size=(30, 30), const="tau", mu=0.5)
    fig = three_dim_plot_flatten(mat, bottom=0, top=0.1)
    np.save("temp", mat)
    plt.savefig("temp.png")


if __name__ == "__main__":
    #run()
    plot(5,"tau",1,"greedy")
