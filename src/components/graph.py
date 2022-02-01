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

    def __repr__(self):
        return "Graph: {}, {}, {}, {}, {}".format(self.vertices, self.edges, self.chi2, self.gradient, self.hessian)

    def __str__(self):
        return "Graph: {}, {}, {}, {}, {}".format(self.vertices, self.edges, self.chi2, self.gradient, self.hessian)

    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def optimise(self):
        pass

    def plot(self, save=False):
        print("Plotting graph...")
        for edge in self.edges:
            edge.plot(self.vertices)
        
        for vertex in self.vertices:
            vertex.plot()
        
        plt.title("GraphSLAM")
        plt.axis("off")
        
        if save:
            print("Saving graph...")
            plt.savefig("graph.pdf")
            print("Graph saved.")
        else:
            print("Showing graph...")
            plt.show()
