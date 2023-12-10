from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def bfs(graph, node):
    parents = {}
    visited = [node]
    queue = [node]
    dist = {node: 0}

    while queue:
        m = queue.pop(0)
        for neighbour in graph[m]:
            if neighbour not in visited:
                parents[neighbour] = m
                dist[neighbour] = dist[m] + 1
                visited.append(neighbour)
                queue.append(neighbour)

    return dist, parents


path = Path("./data")

neighbors = {
    "|": [(0, -1), (0, +1)],  # is a vertical pipe connecting north and south.
    "-": [(-1, 0), (+1, 0)],  # is a horizontal pipe connecting east and west.
    "L": [(0, -1), (+1, 0)],  # is a 90-degree bend connecting north and east.
    "J": [(0, -1), (-1, 0)],  # is a 90-degree bend connecting north and west.
    "7": [(0, +1), (-1, 0)],  # is a 90-degree bend connecting south and west.
    "F": [(0, +1), (+1, 0)],  # is a 90-degree bend connecting south and east.
}

graph = {}
for y, line in enumerate(open(path / "day10.txt")):
    for x, c in enumerate(list(line.strip())):
        if c in neighbors:
            graph[(x, y)] = [(x + dx, y + dy) for dx, dy in neighbors[c]]
        elif c == "S":
            start = (x, y)

graph[start] = [node for node in graph if start in graph[node]]

print(f"Start: {start}")
dist, path = bfs(graph, start)
end, max_dist = dist.popitem()
previous, _ = dist.popitem()

print(max_dist)

plt.scatter(*zip(*graph.keys()))
plt.scatter(*zip(*path), color="orange")
plt.scatter(start[0], start[1], color="red")
for node, edgelist in graph.items():
    for edge in edgelist:
        plt.plot([node[0], edge[0]], [node[1], edge[1]], "k-")

data = []
for dst, src in path.items():
    data.append([src[0], src[1], dst[0], dst[1]])
    plt.plot([src[0], dst[0]], [src[1], dst[1]], "r-")

data.append([end[0], end[1], previous[0], previous[1]])
plt.plot([end[0], previous[0]], [end[1], previous[1]], "r-")

edges = pd.DataFrame(data, columns=["src_x", "src_y", "dst_x", "dst_y"])
vert_edges = edges[edges["src_y"] != edges["dst_y"]]

# Avoid double counting edges
seen_idx = []
inside = []
outside = []
for row in range(y):
    row_edges = vert_edges[
        ((vert_edges["src_y"] == row) | (vert_edges["dst_y"] == row))
        & ~vert_edges.index.isin(seen_idx)
    ]
    for col in range(x):
        crossed = (row_edges["src_x"] > col) | (row_edges["src_x"] > col)

        if (col, row) not in path and (col, row) != start:
            if sum(crossed) % 2 == 0:
                outside.append((col, row))
            else:
                inside.append((col, row))

    seen_idx.extend(row_edges.index.tolist())

plt.scatter(*zip(*inside), color="lime")
print(len(inside))

gap = 0.5
plt.xlim(0 - gap, x + gap)
plt.ylim(0 - gap, y + gap)
plt.xticks(range(x + 1))
plt.yticks(range(y + 1))
plt.gca().invert_yaxis()
plt.savefig("graph.png")
