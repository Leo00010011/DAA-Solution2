import heapq
from vertex import Vertex, make_edge

def slow_solver(graph:list[Vertex],principal_vertex:list[Vertex]):
    edges_matrix = [[0]*len(principal_vertex) for v in principal_vertex]
    distances_matrix = []
    for vertex in principal_vertex:
        vertex.min_edges = [0 for _ in range(len(principal_vertex))]

    for vertex in principal_vertex:
        distances = dijkstra_modificado(graph, vertex)
        distances_matrix.append(distances)

    for vertex in principal_vertex:
        edges_matrix[vertex.Id] = vertex.min_edges
        #print(vertex)
        #print(graph)
        #print()

    edges_matrix = calculate_count_edges(edges_matrix)
    return distances_matrix, edges_matrix

def dijkstra_modificado(graph, start):
    distances = [float('inf') for vertex in graph]
    distances[start.Id] = 0
    visited = [False] * len(graph)

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if visited[current_vertex.Id]:
            continue

        visited[current_vertex.Id] = True

        for neighbor, weight in current_vertex.neighbourhood:
            distance = current_distance + weight
            current_edges = set()
            edge = (current_vertex.Id,neighbor.Id)
            current_edges.add(edge)

            if current_vertex.min_edges[start.Id] != 0:
                current_edges.update(current_vertex.min_edges[start.Id])
            if distance < distances[neighbor.Id]:
                distances[neighbor.Id] = distance
                neighbor.min_edges[start.Id] = current_edges
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor.Id]:
                neighbor.min_edges[start.Id].update(current_edges) 

    return distances

def calculate_count_edges(edges_matrix):
    result = [[0]*len(edges_matrix) for v in edges_matrix] 
    for u, row in enumerate(edges_matrix):
        for v, array in enumerate(row):
            if u == v: continue
            result[u][v] = len(array)
    return result

#graph = {
#    'A': {'B': 5, 'C': 2},
#    'B': {'A': 5, 'C': 3, 'D': 3},
#    'C': {'A': 2, 'B': 3, 'D': 6},
#    'D': {'B': 3, 'C': 6}
#}

#graph = {
#    'A': {'B': 5, 'C': 2,         'array': {'A': 0, 'B': 0, 'C': 0, 'D': 0} },
#    'B': {'A': 5, 'C': 3, 'D': 3, 'array': {'A': 0, 'B': 0, 'C': 0, 'D': 0} },
#    'C': {'A': 2, 'B': 3, 'D': 6, 'array': {'A': 0, 'B': 0, 'C': 0, 'D': 0} },
#    'D': {'B': 3, 'C': 6,         'array': {'A': 0, 'B': 0, 'C': 0, 'D': 0} }
#}
graph = []
for i in range(4):
    v = Vertex()
    graph.append(v)

make_edge(graph[0], graph[1], 5)
make_edge(graph[0], graph[2], 2)
make_edge(graph[1], graph[2], 3)
make_edge(graph[1], graph[3], 3)
make_edge(graph[2], graph[3], 6)

distance, edges = slow_solver(graph, graph)

print("Distancia: ", distance)
print()
print("Aristas: ", edges)
print()