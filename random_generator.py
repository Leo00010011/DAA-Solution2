import random

def random_generator_graph(num_nodes, num_edges, min_weight = 1, max_weight = 10):
    graph = {node: {} for node in range(num_nodes)}
    num_aristas = 0
    graph_sorted = sorted(graph) # poner q ordene de menor a mayor
    while num_aristas < num_edges:
        u, v = random.sample(graph_sorted, 2)
        if v not in graph[u]:
            weight = random.randint(min_weight, max_weight)
            graph[u][v] = weight 
            graph[v][u] = weight
            num_aristas += 1
    for e in graph.values():
        e['array'] = {}
        for node in range(num_nodes):
            e['array'][node] = 0

    return graph

num_nodes = 4
num_edges = 5
graph = random_generator_graph(num_nodes,num_edges)
print(graph)