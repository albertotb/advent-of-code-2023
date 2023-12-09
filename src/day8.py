import math
from itertools import cycle
from pathlib import Path

import pandas as pd

path = Path("./data")

network = {}
with open(path / "day8.txt") as fp:
    inst = list(fp.readline().strip())
    next(fp)
    for line in fp:
        idx, values = line.strip().split(" = ")
        left, right = values.strip("()").split(",")
        network[idx] = {"L": left.strip(), "R": right.strip()}

df = pd.DataFrame(network.values(), index=network.keys())

node = df.index[df.index.str.endswith("A")]
z_iters = pd.Series([0] * len(node), dtype="int")

for n, i in enumerate(cycle(inst)):
    assert len(node) == len(df.loc[node, i])
    node = df.loc[node, i]
    if node.str.endswith("Z").any():
        z_iters[node.str.endswith("Z").reset_index(drop=True)] = n

    if (z_iters > 0).all():
        break

print(z_iters)
print(math.lcm(*(z_iters + 1)))
