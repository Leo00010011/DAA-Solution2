from optimal_solver import optimal_solver
from slow_solver import slow_solver
from random_generator import random_generator_graph
from colorama import Fore, Back, Style
from structures import Vertex
import random
    

def tester(cases_count: int, num_nodes: int, num_edges: int,num_principal:int):
    wrong_answer = []
    for i in range(cases_count):
        graph = random_generator_graph(num_nodes, num_edges)
        principal = random.sample(graph.vertex,num_principal)
        print(f'Caso {i + 1} Graph:\n{graph}')
        _ , actual_edges = optimal_solver(graph,principal)
        _ , real_edges = slow_solver(graph,principal)
        
        if  real_edges != actual_edges:
            print(Fore.RED + f"Error:")
            print("Real Edges")
            print(real_edges) 
            print("Current Edges")
            print(actual_edges)
            wrong_answer.append(graph)
            print(Fore.WHITE)
        else:
            print(Fore.GREEN)
            print("Real Edges")
            print(real_edges) 
            print("Current Edges")
            print(actual_edges)
            print(Fore.WHITE)
        Vertex.Id = 0
    print(f'wrong cases: {len(wrong_answer)}')

tester(100,20,80,5)


