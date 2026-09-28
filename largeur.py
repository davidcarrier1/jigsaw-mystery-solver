import heapq
import time

from puzzle_state import is_solvable, write_log


def heuristic(board, goal_board):
    #Distance de Manhattan
    goal_pos = {tile: i for i, tile in enumerate(goal_board)}
    distance = 0

    for i, tile in enumerate(board):
        if tile != 0:
            row1, col1 = divmod(i, 3)
            row2, col2 = divmod(goal_pos[tile], 3)
            distance += abs(row1 - row2) + abs(col1 - col2)

    return distance


def heuristic2(board, goal_board):
    #Nombre de pièces mal placees
    return sum(
        1
        for i in range(9)
        if board[i] != 0 and board[i] != goal_board[i]
    )


def a_etoile(initial_state, goal_board, log_file=None, h=heuristic):
    start_time = time.time()

    result = None
    nodes_explored = 0
    iteration_log = []

    if not is_solvable(initial_state.board):

        result = None

    else:

        counter = 0  # départage les états de même f (PuzzleState n'a pas de __lt__)
        start_key = tuple(initial_state.board)

        open_list = []
        heapq.heappush(
            open_list,
            (h(initial_state.board, goal_board), counter, 0, initial_state)
        )

        g_score = {start_key: 0}
        closed = set()

        iteration = 0

        while open_list:

            f, _, g, state = heapq.heappop(open_list)

            key = tuple(state.board)

            # Entrée périmée : cet état a déjà été traité avec un meilleur coût
            if key in closed:
                continue

            closed.add(key)
            nodes_explored += 1
            iteration += 1

            if state.board == goal_board:
                result = state
                iteration_log.append(f"{iteration}\t{len(open_list)}")
                break

            for neighbor in state.get_neighbors():

                n_key = tuple(neighbor.board)

                if n_key in closed:
                    continue

                new_g = g + 1

                if new_g < g_score.get(n_key, float("inf")):
                    g_score[n_key] = new_g
                    counter += 1
                    new_f = new_g + h(neighbor.board, goal_board)
                    heapq.heappush(
                        open_list,
                        (new_f, counter, new_g, neighbor)
                    )

            # Taille de la frontière
            iteration_log.append(f"{iteration}\t{len(open_list)}")

    elapsed = time.time() - start_time

    write_log(
        log_file,
        iteration_log,
        nodes_explored,
        elapsed
    )

    return result