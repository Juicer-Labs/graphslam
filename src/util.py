import numpy as np
import matplotlib
matplotlib.use("Qt5Agg")
import matplotlib.pyplot as plt
import csv
import os
import pylab as pl
from matplotlib import collections as mc

def get_data(filename):
    vertices = []
    edge_ids = []
    edges = []
    edges_covariance = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for item in reader:
            if item[0] == "VERTEX2":
                _, _, x,y,yaw = item
                vertices.append((float(x), float(y), float(yaw)))

            if item[0] == "EDGE2":
                # TORO file edge format: EDGE2 IDout IDin dx dy dth I11 I12 I22 I33 I13 I23
                _, IDout, IDin, dx, dy, dth, I11, I12, I22, I33, I13, I23 = item
                edge_ids.append((int(IDout), int(IDin)))
                edges.append((float(dx), float(dy), float(dth)))
                covar = [
                    [I11, I12, I13],
                    [I12, I22, I23],
                    [I13, I23, I33]
                ]
                # TODO(gonk): isn't append wrong, we should do vstack i think - check this
                edges_covariance.append(covar)

    vertices = np.array(vertices)
    edge_ids = np.array(edge_ids)
    edges = np.array(edges)
    edges_covariance = np.array(edges_covariance)

    return vertices, edge_ids, edges, edges_covariance


def draw_data_graph(vertices, edge_ids, edges, edge_covariance):
    # Plot edges
    x1s = []; y1s = []; x2s = []; y2s = []
    
    for id1, id2 in edge_ids:
        x1, y1, _ = vertices[id1]
        x2, y2, _ = vertices[id2]
        x1s.append(x1)
        y1s.append(y1)
        x2s.append(x2)
        y2s.append(y2)

    plt.plot(x1s, y1s, x2s, y2s, marker='')

    # NOTE(gonk): Draw points last so that they're on top
    plt.scatter(vertices[:, 0], vertices[:, 1], s = 10, color='black', marker='o')
    plt.xlabel("X"); plt.ylabel("Y")
    plt.axis('off')
    plt.show()

