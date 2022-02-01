from components.edge import Edge
from components.graph import Graph
from components.vertex import Vertex


def load_graph_file(file):
    """Loads g2o/toro file"""

    vertices = []
    _vertices = []
    edges = []
    _edges = []

    with open(file, 'r') as f:
        for line in f.readlines():
            items = line.split()
            if items[0] == "VERTEX2" or items[0] == "VERTEX_SE2":
                # id = int(items[1])
                vertices.append([float(i) for i in items[2:]])
                # print([float(i) for i in items[2:]])
                _, ID, x, y, theta = items
                v = Vertex(ID, (x, y, theta))
                _vertices.append(v)
                continue

            if items[0] == "EDGE2" or items[0] == "EDGE_SE2":
                _, IDout, IDin, dx, dy, dth, I11, I12, I22, I33, I13, I23 = items
                ids = (int(IDout), int(IDin))
                estimate = (float(dx), float(dy), float(dth))
                covar = [
                    [I11, I12, I13],
                    [I12, I22, I23],
                    [I13, I23, I33]
                ]
                edges.append(Edge(ids, estimate, covar))
                e = Edge(ids, estimate, covar)
                _edges.append(e)
                continue

    # print(vertices)

    # return vertices, edges
    return Graph(_vertices, _edges)
