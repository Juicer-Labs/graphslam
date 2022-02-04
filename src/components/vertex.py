import matplotlib.pyplot as plt


class Vertex(object):

    def __init__(self, id, pose):
        self.id = id
        self.pose = pose  # (x, y, theta)

    ##############
    ### MATHS ###
    ##############

    ##############
    ### DUNDER ###
    ##############

    def __repr__(self):
        return ("Vertex: {}, {}").format(self.id, self.pose)

    def __str__(self):
        return ("Vertex: {}, {}").format(self.id, self.pose)
