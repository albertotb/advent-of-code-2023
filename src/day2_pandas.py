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

    df = pd.DataFrame(
        re.findall("(\d+) (blue|red|green)", cubes), columns=["n", "color"]
    )
    df["n"] = pd.to_numeric(df["n"])
    max_n = df.groupby("color")["n"].max()

    if not (max_n["blue"] > n_blue or max_n["green"] > n_green or max_n["red"] > n_red):
        possible_games.append(int(game.split()[1]))

    power.append(int(math.prod(max_n)))


print(sum(possible_games))
print(sum(power))
