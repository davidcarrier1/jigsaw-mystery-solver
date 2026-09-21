from pathlib import Path

Folder = Path(r"C:\Users\david\OneDrive\Documents\lab ia\jigsaw-mystery-solver\input-Ex1")

TARGET = [1, 2, 3, 4, 5, 6, 7, 8, 0]


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

        # pad short rows (missing trailing tab) with 0 for the empty tile
        while len(row) < 3:
            row.append(0)

        startState.extend(row)

    return startState


def isSolvable(state):
    tiles = [x for x in state if x != 0]
    inversions = sum(1 for i in range(len(tiles)) for j in range(i + 1, len(tiles)) if tiles[i] > tiles[j])
    return inversions % 2 == 0


def depthLimited(state, path, limit, best):
    if state == TARGET:
        return path

    depth = len(path) - 1
    if depth == limit:
        return None

    zero = state.index(0)
    row, col = divmod(zero, 3)
    for move in (-3, 3, -1, 1):
        new_row, new_col = divmod(zero + move, 3)
        if 0 <= new_row < 3 and 0 <= new_col < 3 and abs(row - new_row) + abs(col - new_col) == 1:
            neighbor = state[:]
            neighbor[zero], neighbor[zero + move] = neighbor[zero + move], neighbor[zero]
            key = tuple(neighbor)
            # only go there if it's new, or if we reached it faster than before
            if key not in best or best[key] > depth + 1:
                best[key] = depth + 1
                result = depthLimited(neighbor, path + [neighbor], limit, best)
                if result:
                    return result
    return None


def dfs(startState):
    if not isSolvable(startState):
        return None

    for limit in range(0, 32):  # no 8-puzzle needs more than 31 moves https://www.cs.princeton.edu/courses/archive/spring20/cos226/assignments/8puzzle/checklist.php
        best = {tuple(startState): 0}
        result = depthLimited(startState, [startState], limit, best)
        if result:
            return result
    return None


def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")


files = sorted(Folder.glob("*.txt"))
print(f"Found {len(files)} file(s): {[f.name for f in files]}")

for File in files:
    startState = readState(File)
    print(f"\n=== {File.name} ===")
    print(startState)

    if len(startState) != 9:
        print(f"Expected 9 values, got {len(startState)}. Skipping.")
        continue

    solution = dfs(startState)
    if solution:
        printSolution(solution)
        print(f"Solved in {len(solution) - 1} moves.")
    else:
        print("No solution found.")