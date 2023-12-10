import math
from pathlib import Path

import numpy as np

path = Path("data")

with open(path / "day5.txt") as fp:
    _, seeds = fp.readline().split(":")

    blocks = {}
    for line in fp:
        if line == "\n":
            blockname = next(fp).strip()
            blocks[blockname] = []
        else:
            blocks[blockname].append(line.strip().split())


seedlist = seeds.strip().split(" ")

min_loc = math.inf
for seed in seedlist:
    src = int(seed)
    for block in blocks.values():
        arr = np.array(block).astype("int64")
        mask = (src >= arr[:, 1]) & (src < (arr[:, 1] + arr[:, 2]))
        if sum(mask) == 1:
            src = arr[mask, 0].item() + (src - arr[mask, 1].item())
        elif sum(mask) > 1:
            print("Found several intervals!")

    min_loc = src if src <= min_loc else min_loc

print(min_loc)
