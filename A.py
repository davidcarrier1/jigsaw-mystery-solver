import time

from puzzle_state import is_solvable, write_log

def heuristic(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(board[i] - 1, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def heuristic2(board):
    distance = 0
    for i in range(9):
        if board[i] != 0:
            if board[i] != i + 1:
                distance += 1
    return distance