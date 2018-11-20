from node import *


def find_tile(grid, size, value):
    for row in range(size):
        for col in range(size):
            if grid[row][col] == value:
                return row, col


def swap_tile(grid, r1, c1, r2, c2):
    new = [row[:] for row in grid]
    new[r1][c1] = grid[r2][c2]
    new[r2][c2] = grid[r1][c1]
    return new


def next_moves(node):
    moves = []
    row, col = find_tile(node.grid, Node.size, 0)

    if row > 0 and node.parent_dir != 2:
        grid = swap_tile(node.grid, row, col, row - 1, col)
        moves.append(Node(grid, 1))

    if row < Node.size - 1 and node.parent_dir != 1:
        grid = swap_tile(node.grid, row, col, row + 1, col)
        moves.append(Node(grid, 2))

    if col > 0 and node.parent_dir != 4:
        grid = swap_tile(node.grid, row, col, row, col - 1)
        moves.append(Node(grid, 3))

    if col < Node.size - 1 and node.parent_dir != 3:
        grid = swap_tile(node.grid, row, col, row, col + 1)
        moves.append(Node(grid, 4))

    return moves
