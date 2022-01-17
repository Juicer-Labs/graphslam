import numpy as np
import csv

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
                vertices.append((float(x),float(y),float(yaw)))

            if item[0] == "EDGE2":
                # TORO file edge format:
                # EDGE2 IDout IDin dx dy dth I11 I12 I22 I33 I13 I23
                _, IDout, IDin, dx, dy, dth, I11, I12, I22, I33, I13, I23, _, _ = item
                edge_ids.append((IDout, IDin))
                edges.append((dx, dy, dth))
                covar = [
                    [I11, I12, I13],
                    [I12, I22, I23],
                    [I13, I23, I33]
                ]
                edges_covariance.append(covar)

    vertices = np.array(vertices)
    edge_ids = np.array(edge_ids)
    edges = np.array(edges)
    edges_covariance = np.array(edges_covariance)

    return vertices, edge_ids, edges, edges_covariance

