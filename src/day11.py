from itertools import combinations
from pathlib import Path

import numpy as np

path = Path("./data")

with open(path / "day11.txt") as fp:
    lines = [list(line.strip()) for line in fp.readlines()]

grid = np.array(lines)

# Find galaxies
is_galaxy = grid == "#"
row_idx, col_idx = np.where(is_galaxy)

# Expand coordinates
galaxy_col = is_galaxy.sum(axis=0)
galaxy_row = is_galaxy.sum(axis=1)

# For part 1 `exp_factor = 2`
# We substract one because the original row is replaced by as many rows as
# the expansion factor
# TODO: there is probably a numpy way of doing this
exp_factor = 1000000
for r in range(len(row_idx)):
    row_idx[r] += sum(row_idx[r] > np.flatnonzero(galaxy_row == 0)) * (exp_factor - 1)

for c in range(len(col_idx)):
    col_idx[c] += sum(col_idx[c] > np.flatnonzero(galaxy_col == 0)) * (exp_factor - 1)

# Compute all possible pairs, without taking into account order
pairs = np.array(
    [(r1, c1, r2, c2) for (r1, c1), (r2, c2) in combinations(zip(row_idx, col_idx), 2)]
)

# Compute Manhattan distance
dist = np.abs(pairs[:, 1] - pairs[:, 3]) + np.abs(pairs[:, 0] - pairs[:, 2])

print(pairs.shape)
print(sum(dist))
