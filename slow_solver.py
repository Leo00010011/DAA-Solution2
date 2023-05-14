import heapq
from structures import Vertex, Graph



def slow_solver(graph:Graph,principal_vertex:list[Vertex]):
    edges_matrix = [[0]*len(principal_vertex) for _ in principal_vertex]
    distances_matrix = []

    for vertex in principal_vertex:
        distances_matrix.append(dijkstra(graph, vertex))

    for e,w in graph.edges:
        for ind_s in range(len(principal_vertex)):
            for ind_t in range(ind_s + 1,len(principal_vertex)):
                if(  min(distances_matrix[ind_s][e[0].Id],distances_matrix[ind_s][e[1].Id]) + w 
                   + min(distances_matrix[ind_t][e[0].Id],distances_matrix[ind_t][e[1].Id]) == 
                     distances_matrix[ind_s][principal_vertex[ind_t].Id]):
                    edges_matrix[ind_s][ind_t] += 1
                    
    return distances_matrix, edges_matrix

def dijkstra(graph: Graph, start: Vertex):
    distances = [float('inf') for _ in graph.vertex]
    distances[start.Id] = 0
    visited = [False] * len(graph.vertex)

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if visited[current_vertex.Id]:
            continue
        visited[current_vertex.Id] = True
        for neighbor, weight in current_vertex.neighbourhood:
            distance = current_distance + weight
            if distance < distances[neighbor.Id]:
                distances[neighbor.Id] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances


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
