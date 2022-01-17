import csv

def get_data(filename):
    vertices = []
    edges = []

    with open(filename, 'r') as f:
        reader = csv.reader(f, delimiter=' ')
        for item in reader:
            if item[0] == "VERTEX2":
                vertices.append(item)
            if item[0] == "EDGE2":
                edges.append(item)
    
    return vertices, edges