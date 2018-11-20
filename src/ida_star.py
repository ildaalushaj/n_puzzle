import sys
from next_moves import next_moves


def ida_star(start_node, states, goal):
    threshold = start_node.heuristic()
    solution = []

    def search(node, g, t):
        h = node.heuristic()
        f = g + h
        if f > t:
            return f
        if h == 0:
            return True

        min_val = sys.maxsize
        nodes = next_moves(node)
        states.add_rep(len(nodes))

        for node in nodes:
            states.total_open += 1
            tmp = search(node, g + 1, t)
            if tmp is True:
                solution.insert(0, node.grid)
                states.current_rep -= len(nodes)
                return True
            if tmp < min_val:
                min_val = tmp

        states.current_rep -= len(nodes)
        return min_val

    while True:
        states.current_rep = 1
        threshold = search(start_node, 0, threshold)
        if threshold is True:
            solution.insert(0, start_node.grid)
            return solution
