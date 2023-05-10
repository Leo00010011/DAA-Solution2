from optimal_solver import optimal_solver,graph_to_string
from slow_solver import slow_solver
from random_generator import random_generator_graph
from colorama import Fore, Back, Style
from random import randint
import json
import os.path
    
def tester(cases_count: int, num_nodes: int, num_edges: int,):
    wrong_answer = []
    for i in range(cases_count):
        graph = random_generator_graph(num_nodes, num_edges)
        print(f'Caso {i + 1} Graph = {graph_to_string(graph)}')
        actual_distance, actual_edges = optimal_solver(graph)

        print(f'actual_distance = {actual_distance}')
        print(f'actual_edges = {actual_edges}')
        print()
        real_distance, real_edges = slow_solver(graph)
        print(f'real_distance = {real_distance}')
        print(f'real_edges = {real_edges}')
        print()
        
        with open("tests.txt", "w") as f:
            f.write(f"Graph = {graph_to_string(graph)}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}\n")

        if real_distance != actual_distance or real_edges != actual_edges:
            print(Fore.RED + f"Error: Graph = {graph_to_string(graph)}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}")
            print(Fore.WHITE)
            wrong_answer.append({'graph':graph,'actual_distance':actual_distance,'actual_edges': actual_edges, 'real_distance':real_distance,'real_edges':real_edges})
        else:
            print(Fore.GREEN + f"Graph = {graph_to_string(graph)}, Real Distance = {real_distance}, Real edges = {real_edges}, Actual Distance = {actual_distance}, Actual edges = {actual_edges}\n")
            print(Fore.WHITE)


