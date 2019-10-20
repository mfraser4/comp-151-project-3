"""
Mark Fraser
m_fraser3@u.pacific.edu
COMP 151:  Project 3
"""


class Path(object):
    # construct Path with starting node
    def __init__(self, start):
        super(Path, self).__init__()
        self.path = [start]
        self.length = 0

    def add_node(self, node, length):
        self.path.append(node)
        self.length += length

    def in_path(self, node):
        return node in self.path

    def get_tail_node(self):
        return self.path[len(self.path)-1]

    def copy(self):
        copy = type(self)(self.path[0])
        copy.path = self.path
        copy.length = self.length
        return copy
        