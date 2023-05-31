import matplotlib.pyplot as plt
import numpy as np


def three_dim_plot_flatten(heat_data, bottom=0, top=0.2):
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection="3d")
    x = np.arange(0, 100, 1)
    y = np.arange(0, 100, 1)
    X, Y = np.meshgrid(x, y)
    h, w = heat_data.shape
    Z = np.zeros((100, 100))
    # 値を入れる
    for i in range(h):
        for j in range(w):
            Z[int(100/h*i):int(100/h*(i+1)), int(100/w*j):int(100/w*(j+1))] = heat_data[i][j]

    # プロット
    surf = ax.plot_surface(X, Y, Z)
    # 軸ラベル
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    ax.set_xticks([0, 100])
    ax.set_xticklabels(["0", "1"])
    ax.set_yticks([0, 100])
    ax.set_yticklabels(["0", "1"])
    ax.set_zlim3d(bottom=bottom, top=top)
    return fig
