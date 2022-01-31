#!/usr/bin/env python

import os
import numpy as np

from load import *
from graphslam import *

if __name__ == "__main__":
    # vertices, edge_ids, edges, edges_covariance = get_data(os.path.join(os.path.dirname(__file__), '../data/FRH_P_toro.graph'))
    vertices, edge_ids, edges, edges_covariance = get_data(os.path.join(os.path.dirname(__file__), '../data/input_INTEL_g2o.g2o'))

    info_matrices = get_information_matrix(edges_covariance)

    vertices, _ = graphslam(vertices, info_matrices, edge_ids, edges)
    draw_data_graph(vertices, edge_ids, edges)


