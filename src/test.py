#!/usr/bin/env python
import os
import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import pylab as pl
from matplotlib import collections as mc

from loadgraph import load_graph_file

def draw_data_graph(vertices, edges):
    print(vertices)
    plt.scatter(vertices[:, 0], vertices[:, 1], s=10, marker='o', color='orange', zorder=1)

    # Plot edges
    x1s = []; y1s = []; x2s = []; y2s = []

    for e in edges:
        id1, id2 = e.ids
        x1, y1, _ = vertices[id1]
        x2, y2, _ = vertices[id2]
        x1s.append(x1)
        y1s.append(y1)
        x2s.append(x2)
        y2s.append(y2)

    plt.plot(x1s, y1s, x2s, y2s, marker='', color='green', zorder=0)

    plt.axis('off')
    plt.show()


if __name__ == "__main__":
    vertices, edges = load_graph_file(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))

    vertices = np.array(vertices)
    draw_data_graph(vertices, edges)
