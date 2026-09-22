import time

from puzzle_state import is_solvable, write_log


# ============================================================
# Recherche en profondeur limitée (version itérative, avec pile)
# ============================================================

def _depth_limited_search(initial_state, goal_board, limit, state, iteration_log):
    """
    Effectue une recherche en profondeur limitée à `limit`, en
    partant de `initial_state`. `state` (une liste à un élément)
    contient le compteur global d'itérations, partagé entre les
    différents appels (un par palier de profondeur).
    """

    stack = [initial_state]
    depth_map = {tuple(initial_state.board): 0}

    while stack:

        node = stack.pop()

        state["nodes_explored"] += 1
        state["iteration"] += 1

        if node.board == goal_board:
            iteration_log.append(
                f"{state['iteration']}\t{len(stack)}"
            )
            return node

        depth = depth_map[tuple(node.board)]

        if depth < limit:

            for neighbor in node.get_neighbors():

                key = tuple(neighbor.board)

                if key not in depth_map or depth_map[key] > depth + 1:
                    depth_map[key] = depth + 1
                    stack.append(neighbor)

        # Taille de la frontière (pile) après
        # l'expansion de ce noeud
        iteration_log.append(
            f"{state['iteration']}\t{len(stack)}"
        )

    return None


# ============================================================
# Approfondissement itératif (IDDFS)
# ============================================================

def iddfs(initial_state, goal_board, log_file=None, max_limit=31):
    """
    Approfondissement itératif (Iterative Deepening DFS).

    - initial_state : un PuzzleState (état de départ)
    - goal_board     : la liste représentant l'état objectif
    - log_file       : chemin (Path) où écrire le journal
                       d'exécution, ou None pour ne rien écrire
    - max_limit      : profondeur maximale à essayer (le 8-puzzle
                       possède au maximum une solution de 31
                       mouvements)

    Retourne le PuzzleState final, ou None si aucune solution
    n'a été trouvée.
    """

    start_time = time.time()

    result = None
    iteration_log = []
    state = {"nodes_explored": 0, "iteration": 0}

    if not is_solvable(initial_state.board):

        result = None

    else:

        limit = 0

        while limit <= max_limit:

            result = _depth_limited_search(
                initial_state,
                goal_board,
                limit,
                state,
                iteration_log
            )

            if result is not None:
                break

            limit += 1

    elapsed = time.time() - start_time

    write_log(
        log_file,
        iteration_log,
        state["nodes_explored"],
        elapsed
    )

    return result
