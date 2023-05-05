from queue import PriorityQueue
import os
from astar import *
from mapa import *
from graph import * 

connected_cities = get_connected_cities()
straight_line_cities = get_straight_line_cities()
FaroStraightDistance = get_FaroStraightDistance()


# Verify if the city exists on graph
def verifyCityGraph(city):
    if not city in connected_cities.keys():
        print("Coloque uma cidade válida dentro destas apresentadas: " + ",".join(connected_cities))
        return False
    else:
        return True


# Verify if is a number
def verifyNumber(number):
    if not number.isnumeric():
        print("Coloque um numero válido")
        return False
    else:
        return True


def depth_first(graph, source_city, dest_city):
     visited = set()  # Create an empty set to keep track of visited nodes
     stack = [(source_city, [source_city])]   # Create a stack for DFS

     while stack:
       
        (node, path) = stack.pop()  # remove the last node from the stack
        if node == dest_city:
            print("\nChegamos ao nosso destino, passamos por : ", node)
            break
        print("*" * 100)
        print("\nEstamos na cidade: ", node)
        if node not in visited:
            visited.add(node)   # Add the node to the visited set
            # Add the neighbors of the current node to the
            for neighbor in graph[node]: 
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
        print ("\nCidades visitadas:", path)
     return None


def uniform_cost(graph, origin, destination):
    visitados = set() # conjunto para armazenar nós visitados
    fila = [(0, origin, [])] # fila de prioridade (custo, no_atual, fila de nó)
    
    while True:
        # pop o caminho com o menor custo
        (custo, node, caminho) = min(fila)
        # se o destino for encontrado, retornar caminho
        if node == destination:
            print("\nChegamos ao nosso destino, passamos por: ", caminho + [node])
            print(" \nO custo do caminho foi: ", custo)
            break
        # se não, continuar a busca
        if node not in visitados:
            visitados.add(node)
            # adicionar vizinhos com seus custos ao caminho
            for vizinho, custo_vizinho in graph[node].items(): 
                if vizinho not in visitados:
                    fila.append((custo + custo_vizinho, vizinho, caminho + [node])) #  (soma os custos, node atual, fila dos caminhos visitados)
        fila.remove((custo, node, caminho)) # remove os caminhos visitados anteriormente da fila.
    
    return None


def return_distance(source_city, destination_city, distanceObj):
    return distanceObj.get((source_city, destination_city)) if distanceObj else 1


def heuristic_search(graph, source_city, destination_city, straightDistance):
    border = PriorityQueue()  # cities that does border with city that we are iterating
    border.put((0, source_city, source_city))  # First City
    path_traveled = ""  # final path traveled
    print('\nIteração 0')
    print(source_city)
    i = 1
    while True:

        value, actual_node, path = border.get()  # Get node with the smaller value
        border.queue.clear()  # Delete border cities from last city visited

        if actual_node == destination_city:
            print('-' * 100)
            print('Cidade destino escolhida ' + destination_city)
            print('Caminho percorrido ' + path_traveled + '.')
            print('Fim')
            return

        print('-' * 100)
        print('Iteração ' + str(i))
        for node in graph[actual_node]:
            border.put((return_distance(node, destination_city, straightDistance), node,
                        path + " -> " + node))  # Add border cities to the queue
            path_traveled = str(border.queue[0][2])
        print(sorted(border.queue))  # Sort by value
        if border.queue[0][1] is not destination_city: 
            print('Ir para a cidade: ' + str(border.queue[0][1] + '.'))
        i = i + 1



def menu_profundidade_primeiro():
    origin = ''
    destination = '' 

    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nPor favor, insira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)

    verify_city = False
    while not verify_city:
        destination = input('\nPor favor, insira a cidade de destino: ')
        verify_city = verifyCityGraph(destination)
    
    depth_first(straight_line_cities, origin, destination)
       

def menu_custo_uniforme():

    origin = ''
    destination = '' 
    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nPor favor, insira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)

    verify_city = False
    while not verify_city:
        destination = input('\nPor favor, insira a cidade de destino: ')
        verify_city = verifyCityGraph(destination)
    
    uniform_cost(connected_cities,origin, destination)
    

def menu_procura_sofrega():
    origin = ''
    verify_city = verifyCityGraph(origin)

    while not verify_city:
        origin = input('\nInsira a cidade de origem: ')
        verify_city = verifyCityGraph(origin)
    heuristic_search(straight_line_cities, origin, "Faro", FaroStraightDistance)


def menu_a_star():
    os.system('cls')
    grafo = Grafo()
    grafo.mostrar_cidades()
    verified_key = False

    while not verified_key:
        key = int(input('Por favor, selecione o código correspondente à cidade de origem: '))
        verified_key = grafo.validar_key(key)
        if verified_key:
            os.system('cls')
            print('Vamos começar nossa viagem...')
            busca_estrela = AEstrela(grafo.faro)  # Definindo o objetivo do algoritmo
            cidade_origem = grafo.get_cidade_using_key(key)
            busca_estrela.buscar(cidade_origem)  # Definindo a origem do algoritmo
        else:
            print('O código inserido não é válido.')
        



def Menu():
    print("*" * 100)
    print("Bem vindo")
    while True:
        print("\n")
        print('1 -------------------- Profundidade Primeiro')
        print('2 -------------------- Custo uniforme')
        print('3 -------------------- Procura sôfrega(Destino: Faro)')
        print('4 -------------------- A*(Destino: Faro)')
        print('0 -------------------- Sair')

        method = input('Por favor, escolha o método de procura que deseja: ')

        if method == '1':
            menu_profundidade_primeiro()
        elif method == '2':
            menu_custo_uniforme()
        elif method == '3':
            menu_procura_sofrega()
        elif method == '4':
            menu_a_star()
        elif method == '0':
            print('see you soon =)')
            break
        else:
            print('Opção não válida.')


Menu()

