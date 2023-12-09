from pathlib import Path

import pandas as pd

path = Path("./data")


def extrapolate(seq):
    if (seq == 0).all():
        return 0
    else:
        # part 1
        # return seq.iloc[-1] + extrapolate(seq.diff().dropna())
        return seq.iloc[0] - extrapolate(seq.diff().dropna())


values = []
for line in open(path / "day9.txt"):
    seq = pd.Series(line.strip().split(" ")).astype("int")
    values.append(extrapolate(seq))

print(sum(values))
