from next_moves import next_moves
from algo import Algo
from node import Node
from priority_queue import PriorityQueue, to_tuple


def bfs(start_node, states, goal, algo=Algo.ASTAR):

    closed = {}

    start_node.h = start_node.heuristic()
    start_node.g = 0
    start_node.f = start_node.g + start_node.h

    open_q = PriorityQueue()
    open_q.put(start_node.f, start_node)
    states.total_open += 1
    states.add_rep(1)

    find = False
    while not open_q.empty() and not find:
        parent_node = open_q.get()
        if parent_node.grid == goal:
            find = True
            continue

        closed[to_tuple(parent_node.grid)] = parent_node

        child_nodes = next_moves(parent_node)
        for node in child_nodes:
            g = parent_node.g + 1
            m, h = open_q.is_in_heap(node)
            if not m:
                if to_tuple(node.grid) in closed:
                    m = closed[to_tuple(node.grid)]
            if not m:
                node.update_node(parent_node, g, node.heuristic(), algo)
                open_q.put(node.f, node)
                states.total_open += 1
                states.add_rep(1)
            else:
                if m.g + m.heuristic() > g + node.heuristic():
                    node.update_node(parent_node, g, node.heuristic(), algo)
                    if not h:
                        del closed[to_tuple(m.grid)]
                        open_q.put(node.f, node)
                        states.total_open += 1
                        states.add_rep(1)

    solution = []
    while parent_node:
        solution.append(parent_node.grid)
        parent_node = parent_node.parent_node
    return list(reversed(solution))
