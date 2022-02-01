import numpy as np
import matplotlib.pyplot as plt


class Vertex:

    def __init__(self, id, pose):
        self.id = id
        self.pose = pose  # (x, y, theta)

    def plot(self):
        x, y = self.pose
        plt.plot(x, y, s=10, marker='o', color='orange', zorder=1)
