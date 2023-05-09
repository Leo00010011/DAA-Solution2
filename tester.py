from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import generate_random_weighted_graph_dict
import json
import os.path

def gen_cases(count, num_nodes, num_edges, min_weight = 1, max_weight = 10, rand_func = generate_random_weighted_graph_dict, file_path = 'test.txt'):
    to_save = []
    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path,'r') as fin:
            to_save = json.load(fin)
    for i in range(count):
        graph = rand_func(num_nodes, num_edges)
        print(f'>>>> case {i + 1}')
        print(f'Graph = {graph}')
        distances, edges_ccm = slow_solver(graph)
        print(f'distances = {distances}')
        print(f'edges_ccm = {edges_ccm}')
        to_save.append({'graph': graph, 'distances' : distances, 'edges_ccm': edges_ccm})
        if(i % 10 == 0):
            print(f'{i + 1} cases saved >>>>')
            with open(file_path, 'w') as file:
                json.dump(to_save,file)
    with open(file_path, 'w') as file:
        json.dump(to_save,file)

def json_tester():#file_path = 'test.txt'
    #to_save = []
    #if os.path.exists(file_path) and os.path.isfile(file_path):
    #    with open(file_path,'r') as fin:
    #        to_save = json.load(fin)
    graph = {
        'A': {'B': 5, 'C': 2,         'array': {'B': 0, 'C': 0, 'D': 0} },
        'B': {'A': 5, 'C': 3, 'D': 3, 'array': {'A': 0, 'C': 0, 'D': 0} },
        'C': {'A': 2, 'B': 3, 'D': 6, 'array': {'A': 0, 'B': 0, 'D': 0} },
        'D': {'B': 3, 'C': 6,         'array': {'A': 0, 'B': 0, 'C': 0} }
    }

    distance_optimal, edges_optimal = optimal_solver(graph)
    distance_slow, edges_slow = slow_solver(graph)
    if distance_optimal == distance_slow:
        print("distance_optimal == distance_slow")
    else:
        print("distance_optimal != distance_slow")
    if edges_optimal == edges_slow:
        print("edges_optimal == edges_slow")
    else:
        print("edges_optimal != edges_slow")
    


json_tester()