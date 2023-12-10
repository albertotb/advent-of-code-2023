from pathlib import Path

import pandas as pd

path = Path("example")

with open(path / "day5.txt") as fp:
    _, seeds = fp.readline().split(":")

    blocks = {}
    for line in fp:
        if line == "\n":
            blockname = next(fp).strip()
            blocks[blockname] = []
        else:
            blocks[blockname].append(line.strip().split())

seedlist = [int(s) for s in seeds.strip().split(" ")]

for name in blocks:
    blocks[name] = pd.DataFrame(blocks[name], columns=["dst", "src", "len"]).astype(
        "int64"
    )

location = blocks["humidity-to-location map:"].sort_values(["dst"], ascending=True)

for dst_start, src_start, size in location.itertuples(index=False):
    print(dst_start, src_start, size)
    for src in range(src_start, src_start + size):
        for block in reversed(blocks.values()):
            print(src)
            mask = (src >= block["dst"]) & (src < (block["dst"] + block["len"]))
            if sum(mask) == 1:
                print("--", block.loc[mask, "src"].item())
                src = block.loc[mask, "src"].item() + (
                    src + block.loc[mask, "len"].item()
                )
            elif sum(mask) > 1:
                print("Found several intervals!")
        break
        if src in seedlist:
            print("------Found" + src)
            break
