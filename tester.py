from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import random_generator_graph
from colorama import Fore, Back, Style
from random import randint
import json
import os.path

def gen_cases(count, num_nodes, num_edges, min_weight = 1, max_weight = 10, rand_func = random_generator_graph, file_path = 'test.txt'):
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
    
def tester(cases_count: int, num_nodes: int, num_edges: int):
    wrong_answer = []
    for i in range(cases_count):
        graph = random_generator_graph(num_nodes, num_edges)
        print(f'Caso {i + 1} Graph = {graph}')
        actual_distance, actual_edges = optimal_solver(graph)

        print(f'actual_distance = {actual_distance}')
        print(f'actual_edges = {actual_edges}')
        print()
        real_distance, real_edges = slow_solver(graph)
        print(f'real_distance = {real_distance}')
        print(f'real_edges = {real_edges}')
        print()
        
        with open("tests.txt", "w") as f:
            f.write(f"Graph = {graph}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}\n")

        if real_distance != actual_distance or real_edges != actual_edges:
            print(Fore.RED + f"Error: Graph = {graph}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}")
            print(Fore.WHITE)
            wrong_answer.append({'graph':graph,'actual_distance':actual_distance,'actual_edges': actual_edges, 'real_distance':real_distance,'real_edges':real_edges})
        else:
            print(Fore.GREEN + f"Graph = {graph}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}\n")
            print(Fore.WHITE)


tester(1, 4, 5)