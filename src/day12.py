from itertools import product
from pathlib import Path

import numpy as np

path = Path("./data")

total = 0
for line in open(path / "day12.txt"):
    spring, checksum = line.strip().split(" ")
    codes_check = checksum.split(",")

    arr = np.array(list(spring))
    mask = arr == "?"
    for comb in product("#.", repeat=sum(mask)):
        arr[mask] = comb
        candidate_spring = "".join(arr)
        codes = [str(len(s)) for s in candidate_spring.split(".") if s != ""]
        if codes == codes_check:
            total += 1

print(total)
