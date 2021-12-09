import math

with open('input.txt', 'r') as f:
    heightmap = [list(map(int, l.replace('\n', ''))) for l in f.readlines()]

TOP = 9
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def in_bounds(i, j):
    return i < len(heightmap) and i >= 0 and j < len(heightmap[0]) and j >= 0


def is_low_pt(i, j):
    val = heightmap[i][j]
    adj = []
    for dx, dy in dirs:
        y, x = i + dy, j + dx
        if in_bounds(y, x) and val >= heightmap[y][x]:
            return False

    return True


def dfs(pt):
    stack = [pt]
    seen = set([pt])
    sz = 0

    while stack:
        i, j = stack.pop()
        sz += 1

        for dx, dy in dirs:
            y, x = i + dy, j + dx
            if in_bounds(y, x) and heightmap[y][x] < TOP and (y, x) not in seen:
                seen.add((y, x))
                stack.append((y, x))

    return sz

def main():
    p1, p2 = 0, 0
    low_pts, basin_sizes = [], []

    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if is_low_pt(i, j):
                p1 += heightmap[i][j] + 1
                low_pts.append((i, j))

    for pt in low_pts:
        basin_sizes.append(dfs(pt))
    p2 = math.prod(sorted(basin_sizes, reverse=True)[:3])

    return p1, p2


print(main())
