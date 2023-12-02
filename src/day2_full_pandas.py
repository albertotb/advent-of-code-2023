from pathlib import Path

import pandas as pd

path = Path("data")

df = pd.read_table(path / "day2.txt", sep=":", header=None)

games = (
    df[1]
    .str.extractall("(\d+) (blue|red|green)")
    .reset_index()
    .rename(columns={"level_0": "game", 0: "n", 1: "color"})
    .astype({"n": int, "game": int})
    .assign(game=lambda x: x["game"] + 1)
)

target_max = {"red": 12, "green": 13, "blue": 14}

# Part 1, option 1
games["max"] = games["color"].map(target_max)
games["greater"] = games["n"] > games["max"]
impossible_games = games.groupby("game")["greater"].any()
part1 = sum(impossible_games.index[~impossible_games])
print(part1)

# Part 1, option 2
part1 = (
    games.assign(
        max=lambda x: x["color"].map(target_max), greater=lambda x: x["n"] > x["max"]
    )
    .groupby("game", as_index=False)["greater"]
    .any()
    .loc[lambda x: ~x["greater"], "game"]
    .sum()
)
print(part1)

# Part 2
part2 = games.groupby(["game", "color"])["n"].max().groupby("game").prod().sum()
print(part2)
