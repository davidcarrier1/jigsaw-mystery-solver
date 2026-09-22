from pathlib import Path

Folder = Path(r"C:\Users\david\ia\devoir\jigsaw-mystery-solver\input-Ex1")
TARGET = [1, 2, 3, 4, 5, 6, 7, 8, 0]


def readState(file):
    state = []

    for line in file.read_text(encoding="utf-8").splitlines():
        if line.strip():
            state += [0 if x.strip() == "" else int(x) for x in line.split("\t")]

    return state


def isSolvable(state):
    tiles = [x for x in state if x != 0]
    inversions = sum(tiles[i] > tiles[j]
                     for i in range(8)
                     for j in range(i + 1, 8))
    return inversions % 2 == 0


def dfs(start):
    if not isSolvable(start):
        return None

    stack = [(start, [start])]
    visited = {tuple(start)}

    while stack:
        state, path = stack.pop()

        if state == TARGET:
            return path

        zero = state.index(0)
        row, col = divmod(zero, 3)

        for move in (-1, 1, -3, 3):
            new = zero + move

            if not 0 <= new < 9:
                continue

            new_row, new_col = divmod(new, 3)

            if abs(row - new_row) + abs(col - new_col) != 1:
                continue

            neighbor = state[:]
            neighbor[zero], neighbor[new] = neighbor[new], neighbor[zero]

            if tuple(neighbor) not in visited:
                visited.add(tuple(neighbor))
                stack.append((neighbor, path + [neighbor]))

    return None


def printSolution(path):
    for state in path:
        print("\n".join(" ".join(map(str, state[i:i+3]))
                        for i in range(0, 9, 3)))
        print("-----")


for file in sorted(Folder.glob("*.txt")):
    start = readState(file)

    print(f"\n=== {file.name} ===")
    print(start)

    if len(start) != 9:
        print("État invalide")
        continue

    solution = dfs(start)

    if solution:
        printSolution(solution)
        print(f"Solved in {len(solution) - 1} moves.")
    else:
        print("No solution found.")