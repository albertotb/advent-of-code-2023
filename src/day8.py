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

for n, i in enumerate(cycle(inst)):
    assert node.shape[0] == df.loc[node, i].shape[0]
    node = df.loc[node, i]
    if node.str.endswith("Z").all():
        break
print(n + 1)
