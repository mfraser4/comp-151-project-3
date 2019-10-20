"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 3
"""

from ant import (
    Ant
)

from path import (
    Path
)


infinity = float('inf')
ASCII_OFFSET = 65 # starting character for 'A' in ASCII
MILESTONE = 10    # milestone number of generations to print intermediary output


def get_optimal_path(graph, alpha, beta, rho, num_ants_per_city,
                                                            num_iterations):
    num_cities = len(graph[0])
    best_path = None

    # initialize pheremones for paths
    #   pheremones[i][j] = pheremones[j][i]
    #   pheremones[i][i] has no contextual meaning
    pheremones = [[1.0 for i in range(num_cities)] for j in range(num_cities)]

    for k in range(num_iterations):
        ants = initialize_ants(graph, num_ants_per_city, pheremones, alpha,
                                                                        beta)
        
        # all ants generate path
        #   timing is irrelevant, as nothing is updated until after all ants
        #   have completed their course
        for ant in ants:
            path = ant.generate_path()
            if best_path is None or path.length < best_path.length:
                best_path = path

        # adjust pheremones by evaporation rate
        for i in range(num_cities):
            for j in range(num_cities):
                pheremones[i][j] = (1 - rho) * pheremones[i][j]

        # add pheremones from all ants' paths
        for ant in ants:
            trail = ant.get_pheremone_trail()
            for i in range(num_cities):
                for j in range(num_cities):
                    pheremones[i][j] = pheremones[i][j] + trail[i][j]

        if k % MILESTONE == 0:
            print_statistics(k, ants, best_path)

    return best_path, pheremones


def initialize_ants(graph, num_ants_per_city, pheremones, alpha, beta):
    ants = []
    for city in range(len(graph[0])):
        for i in range(num_ants_per_city):
            ants.append(Ant(graph, pheremones, city, alpha, beta))
    return ants


def print_tour(path):
    path = path.path # for readability
    num_nodes = len(path)
    for i in range(num_nodes):
        if i != num_nodes-1:
            print(chr(path[i] + ASCII_OFFSET) + " -> ", end="")
        else:
            print(chr(path[i] + ASCII_OFFSET) + "\n", end="")


def print_statistics(generation, ants, best_path):
    # extract minimum and maximum paths from ants
    total_length = 0
    min_length = infinity
    max_length = -infinity
    for ant in ants:
        length = ant.path.length
        total_length = total_length + length
        if length < min_length:
            min_length = ant.path.length
        if length > max_length:
            max_length = ant.path.length

    mean_length = total_length / len(ants)

    print("Statistics for generation " + str(generation) + ":")
    print("    local minimum path length:  " + str(min_length))
    print("    local maximum path length:  " + str(max_length))
    print("    local mean path length:     " + str(int(mean_length)))
    print("    global minimum path length: " + str(best_path.length))
    print("    global minimum tour:        ", end="")
    print_tour(best_path)
    print("\n")


def print_pheremone_map(pheremones):
    num_cities = len(pheremones[0])
    print("Pheremone Map:")
    print('{:<8}'.format(''), end="") # buffer for city labeling

    # print city names for column headers
    for i in range(ASCII_OFFSET, ASCII_OFFSET + num_cities):
        entry = '{:<8}'.format(chr(i))
        print(entry, end='')
    print('\n', end='')

    # print rows
    for i in range(num_cities):
        print('{:<8}'.format(chr(ASCII_OFFSET + i)), end='') # print city
        # print pheremone entries
        for p in pheremones[i]:
            entry = '{:<8}'.format(round(p, 2))
            print(entry, end='')
        print('\n', end='')