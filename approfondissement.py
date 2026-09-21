from pathlib import Path

Folder = Path(r"C:\Users\david\OneDrive\Documents\lab ia\jigsaw-mystery-solver\input-Ex1")

queue = []

for File in Folder.glob("*.txt"):
    content = File.read_text(encoding="utf-8")

    # Séparer chaque ligne
    lines = content.splitlines()

    puzzle = []

    for line in lines:
        # Garder les cases vides entre les tabs
        row = line.split("\t")

        # Remplacer une case vide par *
        row = ["*" if x == "" else x for x in row]

        puzzle.extend(row)

    queue.append(puzzle)

print(queue)