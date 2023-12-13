from pathlib import Path

import numpy as np

path = Path("./data")

n = 0
grids = {n: []}
for line in open(path / "day13.txt"):
    if line == "\n":
        n += 1
        grids[n] = []
        continue

    grids[n].append(list(line.strip()))

rows = []
columns = []
for grid in grids.values():
    arr = np.array(grid)
    for r in range(1, arr.shape[0]):
        size = min(r, arr.shape[0] - r)
        top = arr[(r - size) : r, :]
        bottom = arr[r : (r + size), :]
        if (top == np.flip(bottom, axis=0)).all():
            rows.append(r)

    for c in range(1, arr.shape[1]):
        size = min(c, arr.shape[1] - c)
        left = arr[:, (c - size) : c]
        right = arr[:, c : (c + size)]
        if (left == np.flip(right, axis=1)).all():
            columns.append(c)

print(sum(rows) * 100 + sum(columns))
