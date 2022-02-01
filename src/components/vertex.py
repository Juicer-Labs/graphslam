import numpy as np
import matplotlib.pyplot as plt


class Vertex(object):

    def __init__(self, id, pose):
        self.id = id
        self.pose = pose  # (x, y, theta)

    def __repr__(self):
        return "Vertex: {}, {}".format(self.id, self.pose)

    def __str__(self):
        return "Vertex: {}, {}".format(self.id, self.pose)

    def plot(self):
        x, y, _ = self.pose
        # plt.plot(x, y, s=10, marker='o', color='orange', zorder=1)
        plt.plot(x, y, marker='o', color='orange', zorder=1)
