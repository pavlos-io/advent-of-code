with open('input.txt', 'r') as f:
    l = f.read().split(' ')
    y2, y1 = list(map(int, (l[-1].split('=')[1].split('..'))))
    x1, x2 = list(map(int, (l[-2].split('=')[1].replace(',', '').split('..'))))
    # print(y1, y2)

sign = lambda x: (1, -1)[x<0]

def in_target(x, y):
    return x1 <= x <= x2 and y2 <= y <= y1

def sim(x_init, y_init):
    x = 0
    y = 0
    maxy = 0

    while(not in_target(x, y) and x <= x2 and y >= y2):
        x += x_init
        y += y_init
        y_init -= 1

        if x_init > 0:
            x_init -= 1
        maxy = max(maxy, y)

    if in_target(x, y):
        return maxy, True

    return -1, False


def main():
    maxy = 0
    good_inits = set()

    for y in range(y2, 1000):
        for x in range(x2+1):
            _maxy, good = sim(x, y)
            maxy = max(maxy, _maxy)
            if good:
                good_inits.add((x, y))
    
    return maxy, len(good_inits)


print(main())