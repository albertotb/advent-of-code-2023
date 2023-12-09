import math
from pathlib import Path

path = Path("./data")

with open(path / "day6.txt") as fp:
    first, second = fp.readlines()

# part 1
time_list = [int(t) for t in first.split(":")[1].split()]
dist_list = [int(d) for d in second.split(":")[1].split()]

# part 2
time_list = [int("".join(first.split(":")[1].split()))]
dist_list = [int("".join(second.split(":")[1].split()))]

print(time_list)
print(dist_list)

n_wins = []
for race_time, race_dist in zip(time_list, dist_list):
    n = 0
    for i in range(race_time + 1):
        speed = i
        time = race_time - i
        dist = speed * time
        if dist > race_dist:
            n += 1
    n_wins.append(n)

print(math.prod(n_wins))
