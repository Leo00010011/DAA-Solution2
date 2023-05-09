import heapq

def slow_solver(graph):
    for i in range(len(graph)):
        start_vertex = list(graph.items())[i][0]
        distances, edges_ccm = dijkstra(graph, start_vertex)
        for item, v in zip(distances.items(), edges_ccm):
            vertex, distance = item
            print(f'Distancia desde {start_vertex} hasta {vertex}: {distance}')
            print(f'Aristas involucradas: {edges_ccm[v]}')
            
    return distances, edges_ccm

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

#graph = {
#    'A': {'B': 5, 'C': 2},
#    'B': {'A': 5, 'C': 3, 'D': 3},
#    'C': {'A': 2, 'B': 3, 'D': 6},
#    'D': {'B': 3, 'C': 6}
#}

