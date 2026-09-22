import time

from puzzle_state import is_solvable, write_log


# ============================================================
# Recherche en largeur (BFS)
# ============================================================

def bfs(initial_state, goal_board, log_file=None):
    """
    Recherche en largeur (Breadth-First Search).

    - initial_state : un PuzzleState (état de départ)
    - goal_board     : la liste représentant l'état objectif
    - log_file       : chemin (Path) où écrire le journal
                       d'exécution, ou None pour ne rien écrire

    Retourne le PuzzleState final (à partir duquel on peut
    reconstruire le chemin avec get_solution_path), ou None
    si aucune solution n'a été trouvée.
    """

    start_time = time.time()

    result = None
    nodes_explored = 0
    iteration_log = []

    if not is_solvable(initial_state.board):

        result = None

    else:

        queue = [initial_state]
        visited = {tuple(initial_state.board)}

        iteration = 0

        while queue:

            state = queue.pop(0)  # FIFO : on prend le plus ancien état
            nodes_explored += 1
            iteration += 1

            if state.board == goal_board:
                result = state
                iteration_log.append(f"{iteration}\t{len(queue)}")
                break

            for neighbor in state.get_neighbors():

                key = tuple(neighbor.board)

                if key not in visited:
                    visited.add(key)
                    queue.append(neighbor)

            # Taille de la frontière (file d'attente) après
            # l'expansion de cet état
            iteration_log.append(f"{iteration}\t{len(queue)}")

    elapsed = time.time() - start_time

    write_log(
        log_file,
        iteration_log,
        nodes_explored,
        elapsed
    )

    return result
