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
    run()
