import matplotlib
matplotlib.use("Qt5Agg")

import matplotlib.pyplot as plt


class Graph(object):
    
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.chi2 = None
        self.gradient = None
        self.hessian = None

    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def optimise(self):
        pass

    def plot(self):
        print("Plotting graph...")

        for edge in self.edges:
            edge.plot(self.vertices)
        
        for vertex in self.vertices:
            vertex.plot()
        
        plt.title("GraphSLAM")
        plt.axis("off")
        plt.show()
