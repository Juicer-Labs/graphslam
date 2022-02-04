import matplotlib.pyplot as plt
import numpy as np
from edge import Edge

class Graph(object):

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.EPSILON = 0.0004

    #############
    ### MATHS ###
    #############
    def calc_total_error(self):
        """
        Calculates total error of graph - chi2 error (gonk: i think?)
        NOTE(gonk): there's also another possible total error that
        we can caculate as the chi2 error isn't always indicative of a good graph
        """

        total_err = 0
        for edge in self.edges:
            err = edge.calc_error(
                self.vertices[edge.ids[0]*3:edge.ids[0]*3+3],
                self.vertices[edge.ids[1]*3:edge.ids[1]*3+3]
            )
            total_err += np.dot(np.dot(err.T, edge.info_matrix), err)

        return total_err

    def calc_error_gradient_hessian(self):
        pass

    def optimise(self, max_iterations = 50):
        print "initial error: {}\nStarting Optimisation. . .".format(self.calc_total_error())

        # Iterate until convergence or until max_iterations is reached
        for i in range(max_iterations):
            print "iteration #{}".format(i)
            total_err = self.calc_total_error()
            print "current error: {}\n".format(total_err)

            if total_err < self.EPSILON: # Reached convergence
                return

            # BIG NOTE(gonk): WE ARE NOT USING A SPARSE MATRIX THUS WE'RE WASTING A LOT OF MEMORY
            # A BETTER WAY TO STORE THE H MATRIX SHOULD BE THOUGHT OF
            n = len(self.vertices)
            H = np.zeros((n,n), dtype=np.float32)
            b = np.zeros((n,), dtype=np.float32)
            for edge in self.edges:
                i = edge.ids[0]*3
                j = edge.ids[1]*3
                x1 = self.vertices[i:i+3]
                x2 = self.vertices[j:j+3]
                # Note(gonk): Optimisation: calculating the jacobians and error
                # could be done within the same functon since they both use similar
                # intermediate results such as the transformation matrix forms of each pose
                # Calculate Jacobians A, B
                A, B = edge.calc_jacobians(x1, x2)
                err = edge.calc_error(x1, x2)

                # Calculation Hessian matrix and Gradient Vector
                H_ij = np.dot(A.T, np.dot(edge.info_matrix, B))
                H[i:i+3, j:j+3] += H_ij
                H[j:j+3, i:i+3] += H_ij
                H[i:i+3,i:i+3] += np.dot(A.T, np.dot(edge.info_matrix, A))
                H[j:j+3,j:j+3] += np.dot(B.T, np.dot(edge.info_matrix, B))

                b[i:i+3] += -np.dot(err.T, np.dot(edge.info_matrix, A)).T
                b[j:j+3] += -np.dot(err.T, np.dot(edge.info_matrix, B)).T

            H[0:3, 0:3] += np.identity(3)*1000
            # BIG NOTE(gonk): USE SPARSE SOLVER / FASTER METHOD TO SOLVE LINEAR EQUATIONS
            dx = -np.dot(np.linalg.inv(H), b) * 0.000001
            self.vertices += dx

    ###############
    ### DUNDERS ###
    ###############
    def __repr__(self):
        # return "Graph: {}, {}, {}, {}, {}".format(self.vertices, self.edges, self.chi2, self.gradient, self.hessian)
        return "Graph: {}, {}".format(self.vertices, self.edges)

    def __str__(self):
        # return "Graph: {}, {}, {}, {}, {}".format(self.vertices, self.edges, self.chi2, self.gradient, self.hessian)
        return "Graph: {}, {}".format(self.vertices, self.edges)


    ################
    ### PLOTTING ###
    ################

    def plot(self, save=False):
        print("Plotting graph...")

        xs = []; ys = []

        # for vertex in self.vertices:
            # # x, y, _ = vertex.pose
            # x, y, _ = vertex
            # xs.append(x); ys.append(y)

        for vertex in self.vertices.reshape((len(self.vertices)/3, 3)):
            x, y, _ = vertex
            xs.append(x); ys.append(y)

        plt.scatter(xs, ys, s=10, marker='o', color='orange', zorder=1)

        x1s = []; y1s = []; x2s = []; y2s = []

        for edge in self.edges:
            i = edge.ids[0]*3
            j = edge.ids[0]*3
            # x1, y1, _ = self.vertices[id1].pose
            # x2, y2, _ = self.vertices[id2].pose
            x1, y1, _ = self.vertices[i:i+3]
            x2, y2, _ = self.vertices[j:j+3]

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


