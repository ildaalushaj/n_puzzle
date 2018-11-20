import argparse
from check_puzzle import *
from solvable import solvable
from goal import make_goal
from states import States
from bfs import bfs
from ida_star import ida_star
from node import Node
from heuristics import *
from choice_algo import choice_algo
from algo import Algo


def print_states(solution, states):
    for node in solution:
        for line in node:
            print(line)
        print()

    print("total open states: {}".format(states.total_open))
    print("max states: {}".format(states.max_rep))
    print("steps: {}".format(len(solution) - 1))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="n_puzzle file")
    args = parser.parse_args()
    puzzle, size = parse_puzzle(args.file)
    if not check_puzzle(puzzle, size):
        print("Error")
        exit()

    goal = make_goal(size)

    if not solvable(puzzle, goal, size):
        print("This puzzle is not solvable")
        exit()
    else:
        print("This puzzle is solvable\n")

    heuristic, algo = choice_algo()
    states = States()
    Node.size = size
    Node.heuristic_g = Heuristic(size, goal, heuristic)
    start_node = Node(puzzle)

    if start_node.grid == goal:
        solution = [puzzle]
        states.total_open = 1
        states.max_rep = 1
        print_states(solution, states)
        exit()

    if algo == Algo.IDASTAR:
        solution = ida_star(start_node, states, goal)
    else:
        solution = bfs(start_node, states, goal)

    print_states(solution, states)
