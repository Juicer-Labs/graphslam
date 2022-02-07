#!/usr/bin/env python

import os

from components.edge import Edge
from util.load import load_graph_file


def main():
    graph = load_graph_file(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))
    graph.optimise()
    # graph.optimise(max_iterations=2)
    # print('len vertices=%f' % (len(graph.vertices)/3))
    # print('len edges=%i' % len(graph.edges))
    graph.plot(save=True)



if __name__ == "__main__":
    main()
