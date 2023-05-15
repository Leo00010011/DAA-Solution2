import heapq
from structures import Graph, Vertex


def optimal_solver(graph:Graph,principal_vertex:list[Vertex]): 
    # array bidimensional en el que se van a almacenar la respuesta
    edges_matrix = [[0]*len(principal_vertex) for _ in principal_vertex]
    # array de distancias
    distances_matrix = [[0]*len(graph.vertex) for _ in graph.vertex]
    for vertex in graph.vertex:
        # artributo en la que se van a almacenar las aristas 
        # que participan en un camino de costo mínimo que parte
        # desde alguno de los vértices principales
        vertex.min_edges = [0]*len(principal_vertex)

    for vertex_ind, vertex in enumerate(principal_vertex):
        # aquí además de resolver las distancias de los caminos de 
        # costo mínimo que parten de vertex también se calculan 
        # los valores de min_edge de cada vértice correspondientes a 
        # vertex
        distances_matrix[vertex.Id] = dijkstra_modificado(graph, vertex,vertex_ind)
    

    # Por cada combinacion de principal vertex se acumula el valor
    # de min_edges de los vertices que participan en algun camino 
    # de costo mínimo de ese par
    for ind_u in range(len(principal_vertex)):
        u = principal_vertex[ind_u]
        for ind_v in range(ind_u + 1, len(principal_vertex)):
            v = principal_vertex[ind_v]
            edges_count = v.min_edges[ind_u]
            for w in graph.vertex:
                if u == w or v == w: continue
                if distances_matrix[u.Id][w.Id] + distances_matrix[v.Id][w.Id] == distances_matrix[u.Id][v.Id]:
                    edges_count += w.min_edges[ind_u]
            edges_matrix[ind_u][ind_v] = edges_count
    return distances_matrix, edges_matrix


def dijkstra_modificado(graph:Graph, start:Vertex,start_ind):
    distances = [float('inf') for _ in graph.vertex]
    distances[start.Id] = 0
    visited = [False] * len(graph.vertex)
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
                # En el caso de dar menor todas las aristas que se habían contando anteriormente dejan de tener valor
                # y se cuenta la arista responsable de este relax
                neighbor.min_edges[start_ind] = 1
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor.Id]:
                # En caso de que de igual se suma esta arista al conjunto de las aristas que pertenecen a min_edge
                neighbor.min_edges[start_ind] += 1 
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

