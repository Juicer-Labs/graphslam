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

    def plot(self, save=False):
        print("Plotting graph...")

        # TODO (tom): fix this.
        # for edge in self.edges:
        #     edge.plot(self.vertices)
        
        # for vertex in self.vertices:
        #     vertex.plot()

        xs = []; ys = []

        for vertex in self.vertices:
            x, y, _ = vertex.pose
            xs.append(x); ys.append(y)

        plt.scatter(xs, ys, s=10, marker='o', color='orange', zorder=1)

        x1s = []; y1s = []; x2s = []; y2s = []

        for edge in self.edges:
            id1, id2 = edge.ids
            x1, y1, _ = self.vertices[id1].pose
            x2, y2, _ = self.vertices[id2].pose
            
            x1s.append(x1); y1s.append(y1); x2s.append(x2); y2s.append(y2)

        plt.plot(x1s, y1s, x2s, y2s, marker='', color='green', zorder=0)

        plt.title("GraphSLAM")
        plt.axis("off")

        if save:
            print("Saving graph...")
            plt.savefig("graph.pdf")
            print("Graph saved.")

        print("Showing graph...")
        plt.show()
            

    #############
    ### MATHS ###
    #############
    
    def calc_error(self):
        pass

    def calc_error_gradient_hessian(self):
        pass

    def optimise(self):
        pass