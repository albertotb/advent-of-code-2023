from collections import Counter
from pathlib import Path

import numpy as np
import pandas as pd

path = Path("./data")

data = []
for line in open(path / "day7.txt"):
    cards, bid = line.strip().split()
    c = Counter(list(cards))
    try:
        # part 2
        # for part 1, just get the two most common cards
        n_jokers = c["J"]
        del c["J"]
        first, second = c.most_common(2)
        first_val = min(first[1] + n_jokers, 5)
        second_val = second[1] + (n_jokers - (first_val - first[1]))
        assert first_val >= second_val
        assert (first_val + second_val) <= 5
    except ValueError:
        first_val, second_val = 5, 0
    data.append([bid] + list(cards) + [first_val, second_val])

part1 = {"A": "E", "K": "D", "Q": "C", "J": "B", "T": "A"}
part2 = {"A": "E", "K": "D", "Q": "C", "J": "1", "T": "A"}

df = pd.DataFrame(data).fillna(0).astype({6: "int8", 7: "int8"})
df.loc[:, range(1, 6)] = df.loc[:, range(1, 6)].replace(part2)
df_ = df.sort_values(by=[6, 7, 1, 2, 3, 4, 5])
total = (df_.loc[:, 0].astype("int") * np.arange(1, df_.shape[0] + 1)).sum()
print(total)
