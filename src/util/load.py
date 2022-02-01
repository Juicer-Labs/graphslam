import numpy as np

from components.edge import Edge
from components.graph import Graph
from components.vertex import Vertex


def load_graph_file(file):
    """Loads g2o/toro file"""

    vertices = []
    edges = []

    with open(file, 'r') as f:
        for line in f.readlines():
            items = line.split()
            if items[0] == "VERTEX2" or items[0] == "VERTEX_SE2":
                _, ID, x, y, theta = items
                # vertex = Vertex(int(ID), (float(x), float(y), float(theta)))
                # vertices.append(vertex)

                # NOTE(gonk): we dont need a Vertex object as it's just a tuple of 3 floats
                # and the id is just its index in the array - which we might wanna store but
                # for now it's fine
                vertices.append([float(x), float(y), float(theta)])
                continue

            if items[0] == "EDGE2" or items[0] == "EDGE_SE2":
                _, IDout, IDin, dx, dy, dth, I11, I12, I22, I33, I13, I23 = items
                ids = (int(IDout), int(IDin))
                estimate = (float(dx), float(dy), float(dth))
                covar = np.array([[I11, I12, I13], [I12, I22, I23], [I13, I23, I33]], dtype=np.float32)
                edge = Edge(ids, estimate, covar)
                edges.append(edge)
                continue

    return Graph(np.array(vertices, dtype=np.float32), edges)
