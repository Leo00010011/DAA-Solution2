import random
from structures import Vertex, Graph

def random_generator_graph(num_nodes, num_edges, min_weight = 1, max_weight = 10):
    graph = Graph([Vertex() for _ in range(num_nodes)])
    posible_edges = []
    for ind_v, v in enumerate(graph.vertex):
        for u in graph.vertex[ind_v + 1:]:
            posible_edges.append((v,u))
    for _ in range(num_edges):
        u, v = posible_edges.pop(random.randint(0,len(posible_edges) - 1))
        weight = random.randint(min_weight, max_weight)
        graph.make_edge(u,v,weight)
    return graph


