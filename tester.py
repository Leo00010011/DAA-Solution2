from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import gen_cases
import json
import os.path

def gen_cases(count, num_nodes, num_edges, min_weight = 1, max_weight = 10, rand_func = random_generator, file_path = 'test.txt'):
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