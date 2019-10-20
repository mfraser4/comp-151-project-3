"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 3

A swarm optimization algorithm for use in the Travelling Salesman Problem (TSP)
"""


from argparse import (
    ArgumentParser
)

from parseconfig import (
    parse_config
)

from swarm_traveling_salesman import (
    get_optimal_path,
    print_pheremone_map,
    print_tour
)

from sys import (
    exit
)


__author__ = "Mark Fraser"


# main function
#   config - file path of (*.ini) file
def main(config):
    graph, alpha, beta, rho, num_ants_per_city, num_iterations = \
                                                    parse_config(config)

    path, pheremones = get_optimal_path(graph, alpha, beta, rho,
                                            num_ants_per_city, num_iterations)

    # print final results
    print("Results:")
    print("--------\n")
    print("Best Path:")
    print_tour(path)
    print("\n",  end='')
    print("Length:")
    print(path.length)
    print("\n",  end='')
    print_pheremone_map(pheremones)

    # return path for testing purposes
    return path


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", help="Configuration file (*.ini)")
    args = parser.parse_args()

    main(args.config)