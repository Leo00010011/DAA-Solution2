import heapq

class Vertex:
    Id = 0
    def __init__(self):
        self.Id = Vertex.Id
        Vertex.Id = Vertex.Id + 1
        self.neighbourhood : list[(Vertex,int)] = []
        

def make_edge(a:Vertex,b:Vertex,weight:int):
    a.neighbourhood.append((b,weight))
    b.neighbourhood.append((a,weight))



def optimal_solver(graph:list[Vertex],principal_vertex:list[Vertex]): 
    #Primero hago Dijkstra para todos los vertices del grafo
    edges_matrix = []
    distances_matrix = []
    for vertex in graph:
        vertex.min_edges = [0 for _ in range(len(principal_vertex))]
    for vertex in graph:
        distances = dijkstra_modificado(graph, vertex)
        distances_matrix.append(distances)

    for u in graph:
        for v in graph[u.Id + 1:]:
            edges_count = graph[v]['array'][u]
            for w in graph:
                if u == w or v == w: continue
                if distances_matrix[u][w] + distances_matrix[w][v] == distances_matrix[u][v]:
                    edges_count += graph[w]['array'][u]
            if u not in edges_matrix:
                edges_matrix[u] = {}
            edges_matrix[u][v] = edges_count

    for item, edge in zip(distances_matrix.items(), edges_matrix.items()):
        vertex, distance = item
        vertex, vert_count_edges = edge
        #print(f'Distancia desde {vertex} hasta {distance}')
        #print(f'Cantidad de aristas involucradas desde {vertex} hasta {vert_count_edges}')
        #print()
    return distances_matrix, edges_matrix


def dijkstra_modificado(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    visited = set()

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex].items():
            if neighbor == 'array': continue
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                graph[neighbor]['array'][start] = 1 
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor]:
                graph[neighbor]['array'][start] += 1 

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
#distance, edges = optimal_solver(graph)
#
#print("Distancia: ", distance)
#print()
#print("Aristas: ", edges)
