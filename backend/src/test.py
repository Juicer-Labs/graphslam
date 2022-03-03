#!/usr/bin/env python
import os
import numpy as np
from load import load_graph_file
from plot import plot_graph
from slam import optimise_graph

# testing
# from transformation_funcs import t2v, inv_t, v2t, inv_v

def main():
    # vertices, edges = load_graph_file('../data/intel.g2o')
    vertices, edges = load_graph_file('../data/intel_from_mat.g2o')
    optimise_graph(vertices, edges)
    # plot_graph(vertices, edges)

if __name__ == "__main__":
    main()

