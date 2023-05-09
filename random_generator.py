import random

def generate_random_weighted_graph_dict(num_nodes, num_edges, min_weight = 1, max_weight = 10):
    graph = {node: {} for node in range(num_nodes)}
    num_aristas = 0
    while num_aristas < num_edges:
        u, v = random.sample(sorted(graph), 2)
        if v not in graph[u]:
            weight = random.randint(min_weight, max_weight)
            graph[u][v] = weight 
            graph[v][u] = weight # Como el grafo es no dirigido, se agrega la arista en el sentido inverso
            num_aristas += 1
    return graph

num_nodes = 4
num_edges = 5
graph = generate_random_weighted_graph_dict(num_nodes,num_edges)
print(graph)