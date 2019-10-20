"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 3
"""

from configparser import (
    ConfigParser
)

from re import (
    split
)

from sys import (
    exit
)


PARAMETERS = "PARAMETERS"


def parse_config(file):
    config_object = ConfigParser()
    config_object.read(file)

    graph = parse_graph(get_field(config_object, PARAMETERS, "map"))

    alpha = float(get_field(config_object, PARAMETERS, "alpha"))
    assert alpha >= 0, 'alpha value of {} invalid, must be >= 0'.format(alpha)

    beta = float(get_field(config_object, PARAMETERS, "beta"))
    assert beta >= 0, 'beta value of {} invalid, must be >= 0'.format(beta)

    rho = float(get_field(config_object, PARAMETERS, "rho"))
    assert 0 <= rho and rho <= 1, 'rho value of {} invalid, must be in '\
                                                    'range [0,1]'.format(rho)

    num_ants_per_city = int(get_field(config_object, PARAMETERS,
                                                        "num_ants_per_city"))
    assert num_ants_per_city >= 1, 'num_ants_per_city value of {} invalid, '\
                                        'must be >= 1'.format(num_ants_per_city)

    num_iterations = int(get_field(config_object, PARAMETERS, "num_iterations"))
    assert num_iterations >= 1, 'num_iterations value of {} invalid, must be '\
                                                '>= 1'.format(num_iterations)

    return (graph, alpha, beta, rho, num_ants_per_city, num_iterations)


def get_field(config, section, field):
    value = config[section].get(field)
    if value is None or value == "":
        exit(field + " parameter not found")
    return value


def parse_graph(filename):
    file = open(filename, 'r')
    if file is None:
        exit('unable to open ' + filename)

    # process graph file
    contents = file.readlines()
    graph = []
    for line in contents[1:]:
        tmp = split(r'\t+', line)
        tmp = tmp[1:] # strip lettering
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        graph += [tmp]

    # check if matrix is square
    l = len(graph[0])
    for i in range(0,len(graph)):
        if len(graph[i]) != l:
            exit("adjacency matrix is not square:\n" + str(graph))

        for j in range(0,len(graph[i])):
            if i != j and graph[i][j] == 0:
                exit("graph not fully connected at index ({}, {})".format(i, j))

    return graph
