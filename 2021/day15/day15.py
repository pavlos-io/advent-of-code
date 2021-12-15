import heapq, sys

with open('input.txt', 'r') as f:
    risk = [list(map(int, l)) for l in f.read().splitlines()]


dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_risk2():
    m, n = len(risk), len(risk[0])
    m5, n5 = m*5, n*5
    risk2 = [[0] * n5 for _ in range(m5)]

    for i in range(m5):
        for j in range(n5):
            val = 0
            if i < m and j < n:
                val = risk[i][j]
            elif i < m:
                val = risk2[i][j-n] + 1
            elif j < n:
                val = risk2[i-m][j] + 1
            else:
                val = risk2[i-m][j] + 1

            if val > 9:
                val = 1
            risk2[i][j] = val

    return risk2


def in_bounds(i, j, m):
    return i < len(m) and i >= 0 and j < len(m[0]) and j >= 0


def dijkstra(graph, m, n):
    h    = [(0, (0, 0))]
    seen = set([(0, 0)])
    
    while h:
        print(len(h))
        curr_cost, (i, j) = heapq.heappop(h)
        if (i, j) == (m-1, n-1):
            return curr_cost

        for dx, dy in dirs:
            y, x = i + dy, j + dx
            if (y, x) not in seen and in_bounds(y, x, graph):
                seen.add((y, x))
                heapq.heappush(h, (curr_cost + graph[y][x], (y, x)))

    return -1


def main():
    risk2 = get_risk2()

    return dijkstra(risk, len(risk), len(risk[0])), dijkstra(risk2, len(risk2), len(risk2[0]))


print(main())