import random
from optimal_solver import Vertex, make_edge, print_graph

def random_generator_graph(num_nodes, num_edges, min_weight = 1, max_weight = 10):
    graph = [Vertex() for _ in range(num_nodes)]
    num_aristas = 0
    while num_aristas < num_edges:
        u, v = random.sample(graph, 2)
        if v not in [pair[0] for pair in u.neighbourhood]:
            weight = random.randint(min_weight, max_weight)
            make_edge(u,v,weight)
            num_aristas += 1
    return graph

num_nodes = 4
num_edges = 5
graph = random_generator_graph(num_nodes,num_edges)
print_graph(graph)