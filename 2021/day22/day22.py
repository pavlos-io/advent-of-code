from collections import defaultdict
from dataclasses import dataclass
import bisect


@dataclass
class Cuboid:
    xs: list
    ys: list
    zs: list
    state: bool


with open('input.txt', 'r') as f:
    cuboids = []
    for line in f.readlines():
        state, ranges = line.split(' ')
        x, y, z = ranges.split(',')
        cuboids.append(
            Cuboid(
                list(map(int, x[2:].split('..'))),
                list(map(int, y[2:].split('..'))),
                list(map(int, z[2:].split('..'))),
                True if state == 'on' else False
            )
        )


def p1():
    on_off = defaultdict(bool)

    for c in cuboids:
        if c.xs[0] < -50 or c.xs[1] > 50:
            continue
        
        for x in range(c.xs[0], c.xs[1] + 1):
            for y in range(c.ys[0], c.ys[1] + 1):
                for z in range(c.zs[0], c.zs[1] + 1):
                    on_off[(x, y, z)] = c.state

    return len([1 for st in on_off.values() if st])


def get_index(lst, target):
    return bisect.bisect_left(lst, target)
    
    # Custom implementation of bisect.bisect_left aka lower_bound()
    # l, r = 0, len(lst)
    # idx = -1

    # while (l <= r):
    #     m = l + (r-l)//2

    #     if lst[m] >= target:
    #         idx = m
    #         r = m - 1
    #     else:
    #         l = m + 1

    # return idx


# Coordinate Compression
def p2():
    X, Y, Z = [], [], []

    for c in cuboids:
        c.xs[1] += 1
        c.ys[1] += 1
        c.zs[1] += 1

        X.append(c.xs[0])
        X.append(c.xs[1])

        Y.append(c.ys[0])
        Y.append(c.ys[1])

        Z.append(c.zs[0])
        Z.append(c.zs[1])

    X.sort()
    Y.sort()
    Z.sort()

    n = len(X)
    grid = [[[False] * n for _ in range(n)] for _ in range(n)]

    for c in cuboids:
        x0 = get_index(X, c.xs[0])
        x1 = get_index(X, c.xs[1])

        y0 = get_index(Y, c.ys[0])
        y1 = get_index(Y, c.ys[1])

        z0 = get_index(Z, c.zs[0])
        z1 = get_index(Z, c.zs[1])

        for x in range(x0, x1):
            for y in range(y0, y1):
                for z in range(z0, z1):
                    grid[x][y][z] = c.state

    
    sum = 0
    for x in range(n - 1):
        for y in range(n - 1):
            for z in range(n - 1):
                if grid[x][y][z]:
                    sum += (X[x + 1] - X[x]) * (Y[y + 1] - Y[y]) * (Z[z + 1] - Z[z])

    return sum


def main():
    return p1(), p2()



print(main())