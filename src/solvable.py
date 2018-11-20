def countInversion(grid):
    length = len(grid)**2
    row_grid = []
    total = 0

    for y, row in enumerate(grid):
        for x, val in enumerate(row):
            row_grid.append(val)

    for x, val1 in enumerate(row_grid):
        for y in range(x + 1, length):
            val2 = row_grid[y]
            if (val1 > val2 and val1 != 0 and val2 != 0):
                total += 1
    return total


def transform(puzzle):
    size = len(puzzle)
    index = [None] * (size**2)
    for y in range(size):
        for x in range(size):
            i = puzzle[y][x]
            index[i] = (y, x)
    return index


def solvable(puzzle, goal, size):
    puzzle_inversions = countInversion(puzzle)
    goal_inversions = countInversion(goal)
    copy_puzzle = transform(puzzle)
    copy_goal = transform(goal)
    if (size % 2 == 0):  # In this case, the row of the '0' is important
        puzzle_inversions += copy_puzzle[0][0]
        goal_inversions += copy_goal[0][0]
    return (puzzle_inversions % 2 == goal_inversions % 2)
