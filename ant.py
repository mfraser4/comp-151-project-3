"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 3
"""


from path import (
    Path
)

from random import (
    random
)


class Ant(object):
    PHEREMONE = 100 # amount of pheremone an individual ant can lay

    # construct Ant with starting city and amount of pheremone
    def __init__(self, graph, pheremones, starting_city, alpha, beta):
        super(Ant, self).__init__()
        self.graph = graph
        self.pheremones = pheremones
        self.path = Path(starting_city)
        self.alpha = alpha
        self.beta =  beta

    def generate_path(self):
        num_steps = len(self.graph[0])-1
        for i in range(num_steps):
            curr_city = self.path.get_tail_node()
            cities = self._get_available_cities()

            # randomly select next city to go to based on probability function
            prob = 0
            result = random()
            for city in cities:
                prob = prob + \
                            self._calculate_probability(curr_city, city, cities)
                if result <= prob:
                    self.path.add_node(city, self.graph[curr_city][city])
                    break
        return self.path

    def get_pheremone_trail(self):
        path = self.path.path # for readability
        num_nodes = len(path)
        pheremones = [[0 for i in range(num_nodes)] for j in range(num_nodes)]
        # add pheremones in appropriate proportions to corresponding path entry
        for i in range(num_nodes-1):
            start = path[i]
            end = path[i+1]
            pheremones[start][end] = self.PHEREMONE / self.path.length
            pheremones[end][start] = self.PHEREMONE / self.path.length
        return pheremones

    # returns all cities not traversed in ant's currently stored path
    def _get_available_cities(self):
        cities = []
        for i in range(len(self.graph[0])):
            if not self.path.in_path(i):
                cities.append(i)
        return cities

    # calculates probability of traversing to j provided the path's pheremone
    # level and distance from i to j and the set of available cities
    def _calculate_probability(self, i, j, cities):
        total = 0
        for c in cities:
            total = total + ((self.pheremones[i][c]**self.alpha) * \
                                        ((1 / self.graph[i][c])**self.beta))
        probability = ((self.pheremones[i][j]**self.alpha) * \
                                    ((1 / self.graph[i][j])**self.beta)) / total
        return probability