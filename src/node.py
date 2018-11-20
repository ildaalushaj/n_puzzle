import sys
from algo import Algo


class Node:
    size = 0
    heuristic_g = None

    def __init__(self, grid, parent_dir=0, g=sys.maxsize, h=sys.maxsize):
        self.grid = grid
        self.parent_node = None
        self.parent_dir = parent_dir
        self.g = g
        self.h = h
        self.f = 0

    def heuristic(self):
        return self.heuristic_g.distance(self.grid)

    def update_node(self, parent_node, g, h, algo):
        self.parent_node = parent_node
        self.g = g
        self.h = h

        if algo == Algo.ASTAR:
            self.f = g + h
        elif algo == Algo.GREEDY:
            self.f = h
        else:  # algo == Algo.UNIFROME
            self.f = g
