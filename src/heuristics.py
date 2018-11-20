from math import *

class Heuristic:
    def __init__(self, size, goal, heuristic):
        self.heuristic = None
        self.size = size
        self.goal_index_position = [None] * size**2
        self.puzzle = [None] * size**2
        self._index_position(goal, self.goal_index_position)
        self.init_heuristic(heuristic)

    def _index_position(self, grid, index):
        for y in range(self.size):
            for x in range(self.size):
                i = grid[y][x]
                index[i] = (y, x)

    def manhattan(self, grid):
        self._index_position(grid, self.puzzle)

        distance = 0
        for a, b in zip(self.goal_index_position[1:], self.puzzle[1:]):
            distance += abs(a[0] - b[0]) + abs(a[1] - b[1])
        return distance

    def euclidian(self, grid):
        self._index_position(grid, self.puzzle)

        distance = 0
        for a, b in zip(self.goal_index_position[1:], self.puzzle[1:]):
            distance_x = abs(a[0] - b[0])
            distance_y = abs(a[1] - b[1])
            distance += sqrt(distance_x * distance_x + distance_y * distance_y)
        return int(distance)

    def uniform(self, grid):
        return 0

    def misplaced(self, grid):
        self._index_position(grid, self.puzzle)

        distance = 0
        for a, b in zip(self.goal_index_position[1:], self.puzzle[1:]):
            if a != b:
                distance += 1
        return distance

    def init_heuristic(self, heuristic):
        if heuristic == 'Manhattan Distance':
            self.heuristic = self.manhattan
        elif heuristic == 'Misplaced Tiles':
            self.heuristic = self.misplaced
        elif heuristic == 'Euclidian Distance':
            self.heuristic = self.euclidian
        else:
            self.heuristic = self.uniform

    def distance(self, grid):
        return self.heuristic(grid)
