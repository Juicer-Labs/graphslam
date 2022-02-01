#!/usr/bin/env python

import os
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt

from matplotlib import collections as mc
from util.load import load_graph_file

from components.edge import Edge


def draw_data_graph(vertices, edges):
    # print(vertices)

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


def main():
    # e = Edge(None, None, None, False)
    # e.plot()
    graph = load_graph_file(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))
    graph.plot()


if __name__ == "__main__":
    # vertices, edges = load_graph_file(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))
    # graph = load_graph_file(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))
    # graph.plot()

    # vertices = np.array(vertices)
    # draw_data_graph(vertices, edges)

    main()
