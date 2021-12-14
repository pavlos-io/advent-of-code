with open('input.txt', 'r') as f:
    pts, instructions = f.read().split('\n\n')
    pts = set([tuple(map(int, c.split(','))) for c in pts.split('\n')])
    instructions = [i.split(' ')[-1] for i in instructions.split('\n')]


r = max(pts, key=lambda p: p[0])[0]
d = max(pts, key=lambda p: p[1])[1]


def foldy(y_line):
    global d
    new_pts = set()
    for x, y in pts:
        if y > y_line:
            new_pts.add((x, y_line - (y - y_line)))
    d = y_line - 1
    pts.update(new_pts)


def foldx(x_line):
    global r
    new_pts = set()
    for x, y in pts:
        if x > x_line:
            new_pts.add((x_line - (x - x_line), y))
    r = x_line - 1
    pts.update(new_pts)


def fold(dir, val):
    if dir == 'x':
        foldx(val)
    elif dir == 'y':
        foldy(val)


def count_pts():
    return len(
        [1 for x, y in pts if x <= r and y <= d]
    )

def main():
    for i, ins in enumerate(instructions):
        dir, val = ins.split('=')

        fold(dir, int(val))
        
        if i == 0:
            print(count_pts()) #p1

    # p2
    for i in range(d+1):
        print('')
        for j in range(r+1):
            if (j,i) in pts:
                print('#', end="")
            else:
                print('.', end="")

main()