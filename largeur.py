from pathlib import Path

Folder = Path(r"C:\Users\david\OneDrive\Documents\lab ia\jigsaw-mystery-solver\input-Ex1")


def readState(File):
    content = File.read_text(encoding="utf-8")
    startState = []

    for line in content.splitlines():
        if not line.strip():          
            continue
        values = line.split("\t")

        for value in values:
            value = value.strip()
            if value == "":
                startState.append(0)
            else:
                startState.append(int(value))

    return startState


def bfs(startState):
    target = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    queue = [startState]
    visited = {tuple(startState): None}

    while queue:
        state = queue.pop(0)  # FIFO: take the oldest state (front of the list)
        if state == target:
            path = []
            while state:
                path.append(state)
                state = visited[tuple(state)]
            return path[::-1]

        zero = state.index(0)
        row, col = divmod(zero, 3)
        for move in (-3, 3, -1, 1):
            new_row, new_col = divmod(zero + move, 3)
            if 0 <= new_row < 3 and 0 <= new_col < 3 and abs(row - new_row) + abs(col - new_col) == 1:
                neighbor = state[:]
                neighbor[zero], neighbor[zero + move] = neighbor[zero + move], neighbor[zero]
                if tuple(neighbor) not in visited:
                    visited[tuple(neighbor)] = state
                    queue.append(neighbor)

    return None


def printSolution(path):
    for state in path:
        print("\n".join(' '.join(map(str, state[i:i+3])) for i in range(0, 9, 3)), end="\n-----\n")


for File in Folder.glob("*.txt"):
    startState = readState(File)
    print(f"\n=== {File.name} ===")
    print(startState)

    if len(startState) != 9:
        print(f"Expected 9 values, got {len(startState)}. Skipping.")
        continue

    solution = bfs(startState)
    if solution:
        printSolution(solution)
        print(f"Solved in {len(solution) - 1} moves.")
    else:
        print("No solution found.")