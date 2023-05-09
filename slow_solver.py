import heapq

def slow_solver(graph):
    edges_matrix = {}
    distances_matrix = {}

    for i in range(len(graph)):
        start_vertex = list(graph.items())[i][0]
        distances, edges_ccm = dijkstra(graph, start_vertex)
        distances_matrix[start_vertex] = distances
        edges_matrix[start_vertex] = edges_ccm
        #print(start_vertex)
        #print(graph)
        #print()

    edges_matrix = calculate_count_edges(edges_matrix)
    return distances_matrix, edges_matrix

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    edges_ccm = {vertex: set() for vertex in graph}
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
            current_edges = set()
            edge = (current_vertex,neighbor)
            current_edges.add(edge)

            if len(edges_ccm[current_vertex]) != 0:
                current_edges.update(edges_ccm[current_vertex])
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                edges_ccm[neighbor] = current_edges
                heapq.heappush(priority_queue, (distance, neighbor))
            elif distance == distances[neighbor]:
                edges_ccm[neighbor].update(current_edges)

    return distances, edges_ccm

def calculate_count_edges(edges_matrix):
    result = {}
    
    for u, array in edges_matrix.items():
        result[u] = {}
        for v in array:
            if u == v: continue
            result[u][v] = len(array[v])

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

#distance, edges = slow_solver(graph)

#print("Distancia: ", distance)
#print()
#print("Aristas: ", edges)
#print()