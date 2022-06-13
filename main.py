import networkx as nx
from matplotlib import pyplot as plt

from src.PageRank import PageRank

import numpy as np
import os

archivo = "dataset1"


def algoritmo(iteration, graph, damping_factor, result_dir, fname):
    pagerank_fname = '_resultado.txt'

    PageRank(graph, damping_factor, iteration)
    pagerank_list = graph.get_pagerank_list()
    print('Algoritmo:')
    print(pagerank_list)
    print()
    path = os.path.join(result_dir, fname)
    os.makedirs(path, exist_ok=True)
    np.savetxt(os.path.join(path, fname + pagerank_fname), pagerank_list, fmt='%.3f', newline=" ")


if __name__ == '__main__':

    with open('./dataset/dataset2.txt') as f:
        lines = f.readlines()

    G = nx.DiGraph()

    for line in lines:
        t = tuple(line.strip().split(','))
        G.add_edge(*t)

    pr = nx.pagerank(G)
    pr = dict(sorted(pr.items(), key=lambda x: x[0]))
    print(np.round(list(pr.values()), 3))

    nx.draw(G, with_labels=True, node_size=2000, edge_color='#eb4034', width=3, font_size=16, font_weight=500,
            arrowsize=20,
            alpha=0.8)
    plt.savefig("grafo.png")
