from algo import Algo

def choice_algo():
    heuristic = None
    algo_list = {'1': 'IDA*', '2': 'A*', '3': 'Greedy', '4': 'Uniform cost'}
    choice = input("Choose between the following algos to solve the problem :"
                   "\n 1: 'IDA*'\n 2: 'A*'\n 3: 'Greedy'\n 4: 'Uniform cost'\n"
                   "Enter a number (1, 2, 3 or 4): ")
    if choice in algo_list:
        algo = algo_list[choice]
    else:
        print("Not a correct value")
        exit()
    print("\nYou choose:\n{}\n".format(algo))

    if algo == 'A*':
        algo = Algo.ASTAR
    elif algo == 'Greedy':
        algo = Algo.GREEDY
    elif algo == 'IDA*':
        algo = Algo.IDASTAR
    else:
        algo = Algo.UNIFORME

    if algo != Algo.UNIFORME:
        heuristic_list = {'1': 'Manhattan Distance', '2': 'Misplaced Tiles', '3': 'Euclidian Distance'}
        choice = input("Choose between the 3 following heuristics to solve the problem :\n"
                       " 1: 'Manhattan Distance'\n 2: 'Misplaced Tiles'\n 3: 'Euclidian Distance'\n"
                       "Enter a number (1, 2, or 3): ")
        if choice in heuristic_list:
            heuristic = heuristic_list[choice]
            print("\nYou choose:\n{}\n".format(heuristic))
        else:
            print("Not a correct value")
            exit()

    return heuristic, algo
