from pathlib import Path


# ============================================================
# Configuration
# ============================================================

Folder = Path(r"C:\Users\david\ia\devoir\jigsaw-mystery-solver\input-Ex1")

TARGET = [1, 2, 3, 4, 5, 6, 7, 8, 0]


# ============================================================
# Lecture d'un fichier
# ============================================================

def readState(File):

    content = File.read_text(encoding="utf-8")

    startState = []

    for line in content.splitlines():

        if not line.strip():
            continue

        values = line.split("\t")

        row = []

        for value in values:

            value = value.strip()

            row.append(0 if value == "" else int(value))

        # Ajouter des 0 si la dernière case est absente
        while len(row) < 3:
            row.append(0)

        startState.extend(row)

    return startState


# ============================================================
# Vérifier si le puzzle est solvable
# ============================================================

def isSolvable(state):

    # On enlève la case vide
    tiles = [x for x in state if x != 0]

    # Compter les inversions
    inversions = sum(
        1
        for i in range(len(tiles))
        for j in range(i + 1, len(tiles))
        if tiles[i] > tiles[j]
    )

    # Pour un puzzle 3x3, le nombre d'inversions
    # doit être pair pour que le puzzle soit solvable.
    return inversions % 2 == 0


# ============================================================
# Recherche en profondeur limitée
# ============================================================

def depthLimitedSearch(state, path, limit, visited):

    # Si on atteint la solution
    if state == TARGET:
        return path

    # Profondeur actuelle
    depth = len(path) - 1

    # Ne pas dépasser la limite de profondeur
    if depth == limit:
        return None

    # Position de la case vide
    zero = state.index(0)

    row, col = divmod(zero, 3)

    # Déplacements possibles :
    # -3 = haut
    # +3 = bas
    # -1 = gauche
    # +1 = droite
    for move in (-3, 3, -1, 1):

        new_zero = zero + move

        # Vérifier que la nouvelle position est dans le tableau
        if not (0 <= new_zero < 9):
            continue

        new_row, new_col = divmod(new_zero, 3)

        # Vérifier que le déplacement est réellement adjacent.
        # Cela empêche par exemple de passer directement
        # de la colonne 0 à la colonne 2.
        if abs(row - new_row) + abs(col - new_col) != 1:
            continue

        # Créer le nouvel état
        neighbor = state[:]

        neighbor[zero], neighbor[new_zero] = \
            neighbor[new_zero], neighbor[zero]

        key = tuple(neighbor)

        # Ne visiter l'état que s'il est nouveau
        # ou si on l'atteint avec moins de mouvements.
        if key not in visited or visited[key] > depth + 1:

            visited[key] = depth + 1

            result = depthLimitedSearch(
                neighbor,
                path + [neighbor],
                limit,
                visited
            )

            # Solution trouvée
            if result is not None:
                return result

    return None


# ============================================================
# Approfondissement itératif
# ============================================================

def iterativeDeepening(startState):

    # Vérifier si le puzzle est solvable
    if not isSolvable(startState):
        return None

    # Le 8-puzzle possède au maximum une solution
    # de 31 mouvements.
    limit = 0

    while limit <= 31:

        print(f"Recherche avec profondeur maximale = {limit}")

        # On recommence une nouvelle recherche pour
        # chaque nouvelle profondeur.
        visited = {
            tuple(startState): 0
        }

        result = depthLimitedSearch(
            startState,
            [startState],
            limit,
            visited
        )

        # Si une solution est trouvée, on arrête.
        if result is not None:
            return result

        # Sinon, on augmente la profondeur maximale.
        limit += 1

    return None


# ============================================================
# Affichage de la solution
# ============================================================

def printSolution(path):

    for state in path:

        print(
            "\n".join(
                " ".join(map(str, state[i:i + 3]))
                for i in range(0, 9, 3)
            ),
            end="\n-----\n"
        )


# ============================================================
# Programme principal
# ============================================================

files = sorted(Folder.glob("*.txt"))

print(f"Found {len(files)} file(s): {[f.name for f in files]}")


for File in files:

    startState = readState(File)

    print(f"\n=== {File.name} ===")
    print(startState)

    # Vérifier que l'état contient exactement 9 cases
    if len(startState) != 9:

        print(
            f"Expected 9 values, got {len(startState)}. Skipping."
        )

        continue

    # Résoudre avec l'approfondissement itératif
    solution = iterativeDeepening(startState)

    if solution:

        printSolution(solution)

        print(
            f"Solved in {len(solution) - 1} moves."
        )

    else:

        print("No solution found.")

