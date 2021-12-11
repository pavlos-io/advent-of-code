with open('input.txt', 'r') as f:
    lines = [list(map(int, l)) for l in f.read().splitlines()]

CYCLE = 9
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]


def gain_energy():
    will_flash = []
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            lines[i][j] += 1
            if lines[i][j] > CYCLE:
                will_flash.append((i, j))
    
    return will_flash


def show():
    print('')
    for row in lines:
        print('')
        for cell in row:
            print(cell, end="")


def in_bounds(i, j):
    return len(lines) > i >= 0 and len(lines[0]) > j >= 0


def dfs(init_stack):
    stack = init_stack
    seen  = set(init_stack)

    while stack:
        i, j = stack.pop()

        for dy, dx in dirs:
            y, x = i + dy, j + dx
            if in_bounds(y, x):
                lines[y][x] += 1
                if lines[y][x] > CYCLE and (y, x) not in seen:
                    stack.append((y, x))
                    seen.add((y, x))


def get_flash_count_and_reset():
    count = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] > CYCLE:
                lines[i][j] = 0
                count += 1

    return count


def main():
    p1, p2 = 0, 0
    day = 0

    while True:
        day += 1
        if will_flash := gain_energy():
            dfs(will_flash)
            count = get_flash_count_and_reset()
            
            if day <= 100:
                p1 += count
            
            if count == len(lines) * len(lines[0]):
                p2 = day
                break
        # show()

    return p1, p2

print(main())