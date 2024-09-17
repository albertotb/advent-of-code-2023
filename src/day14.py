from pathlib import Path

import numpy as np

path = Path("./example")

grid = np.array([list(line.strip()) for line in open(path / "day14.txt")])


print(grid)

print((grid == "O").sum(axis=0))
