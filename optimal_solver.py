import heapq
from vertex import Vertex, make_edge

def optimal_solver(graph:list[Vertex],principal_vertex:list[Vertex]): 
    #Primero hago Dijkstra para todos los vertices del grafo
    edges_matrix = [[0]*len(principal_vertex) for v in principal_vertex]
    distances_matrix = []
    for vertex in graph:
        vertex.min_edges = [0 for _ in range(len(principal_vertex))]
    for vertex in graph:
        distances = dijkstra_modificado(graph, vertex)
        distances_matrix.append(distances)

    for u in graph:
        for v in graph[u.Id + 1:]:
            edges_count = v.min_edges[u.Id]
            for w in graph:
                if u == w or v == w: continue
                if distances_matrix[u.Id][w.Id] + distances_matrix[w.Id][v.Id] == distances_matrix[u.Id][v.Id]:
                    edges_count += w.min_edges[u.Id]
            edges_matrix[u.Id][v.Id] = edges_count

    for vertex, distance  in enumerate(distances_matrix):
        print(f'Distancia desde {vertex} hasta {distance}')
        
        print()
    for vertex, edge  in enumerate(edges_matrix):
        print(f'Cantidad de aristas involucradas desde {vertex} hasta {edge}')

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

        for neighbor, weight  in current_vertex.neighbourhood:
            distance = current_distance + weight
            
            if distance < distances[neighbor.Id]:
                distances[neighbor.Id] = distance
                neighbor.min_edges[start.Id] = 1 
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor.Id]:
                neighbor.min_edges[start.Id]  += 1 

    return distances

# Cada vertice tiene los costos de sus aristas con sus respectivos adyacentes y un diccionario
# de todos lo vertices con las respectivas cantidades de aristas que llegan al él en un CCM.

#graph = {
#    'A': {'B': 5, 'C': 2,         'array': {'B': 0, 'C': 0, 'D': 0} },
#    'B': {'A': 5, 'C': 3, 'D': 3, 'array': {'A': 0, 'C': 0, 'D': 0} },
#    'C': {'A': 2, 'B': 3, 'D': 6, 'array': {'A': 0, 'B': 0, 'D': 0} },
#    'D': {'B': 3, 'C': 6,         'array': {'A': 0, 'B': 0, 'C': 0} }
#}

#distances_matrix = {}
#edges_matrix = { 
#    'A': {'A': 0, 'B': 0, 'C': 0, 'D': 0 },
#    'B': {'A': 0, 'B': 0, 'C': 0, 'D': 0 },
#    'C': {'A': 0, 'B': 0, 'C': 0, 'D': 0 },
#    'D': {'A': 0, 'B': 0, 'C': 0, 'D': 0 }
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


distance, edges = optimal_solver(graph,graph)

print("Distancia: ", distance)
print()
print("Aristas: ", edges)
