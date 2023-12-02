import math
import re
from pathlib import Path

import pandas as pd

path = Path("data")

n_red, n_green, n_blue = 12, 13, 14

possible_games = []
power = []
for line in open(path / "day2.txt"):
    game, cubes = line.split(":")

    data = []
    for c in cubes.split(";"):
        round = {}
        for m in re.finditer("(\d+) (blue|red|green)", c):
            if m:
                round[m.group(2)] = int(m.group(1))
        data.append(round)

    df = pd.DataFrame(data)
    if not (
        df["blue"].max() > n_blue
        or df["green"].max() > n_green
        or df["red"].max() > n_red
    ):
        possible_games.append(int(game.split()[1]))

    power.append(int(math.prod(df.max())))


print(possible_games)
print(sum(possible_games))
print(sum(power))
