from collections import defaultdict
from itertools import permutations
from types import new_class

with open('input.txt', 'r') as f:
    algo, img = f.read().split('\n\n')
    img = [row for row in img.split('\n')]

DARK  = '.'
LIGHT = '#'

pxl_to_bin = {
    DARK: '0',
    LIGHT: '1'
}

dirs = [
    [(-1, -1), (-1, 0), (-1, 1)],
    [(0, -1), (0, 0), (0, 1)],
    [(1, -1), (1, 0), (1, 1)],
]

rest = LIGHT


def in_bounds(i, j, m):
    return i < len(m) and i >= 0 and j < len(m[0]) and j >= 0


def show(img):
    for i in range(len(img)):
        print('')
        for j in range(-4, len(img[0]) + 4):
            if in_bounds(i, j, img):
                print(img[i][j], end="")
            else:
                print('.', end="")
    print('')


def translate(idx, dim):
    if idx == 0:
        idx = -1
    elif idx == dim + 1:
        idx = dim
    else: 
        idx = idx - 1
    
    return idx


def get_next_template(m, n):
    next_img = [[None for _ in range(n + 2)] for _ in range(m + 2)]
    
    for i in range(len(next_img)):
        y = translate(i, m)
        for j in range(len(next_img[0])):
            x = translate(j, n)
            next_img[i][j] = (y, x)

    return next_img

def get_rest():
    global rest
    if algo[0] == LIGHT:
        print(rest, LIGHT if rest == DARK else DARK)
        rest = LIGHT if rest == DARK else DARK
    else:
        rest = DARK
    print(rest)
    return rest

def get_pxl_row(pt, row, r):
    i, j = pt
    s = ""
    for dy, dx in row:
        y, x = i + dy, j + dx
        rest = DARK if r % 2 else LIGHT
        el = img[y][x] if in_bounds(y, x, img) else rest
        s += pxl_to_bin[el]
    return s


def get_next_pxl(pt, r):
    s = ""
    for row in dirs:
        s += get_pxl_row(pt, row, r)
    num = int(s, 2)
    
    return algo[num]


def get_lit_pxl_count(img):
    return len([1 for row in img for el in row if el == LIGHT])
    

def main():
    global img
    for r in range(50):
        next_img = get_next_template(len(img), len(img[0]))

        for i in range(len(next_img)):
            for j in range(len(next_img[0])):
                next_img[i][j] = get_next_pxl(next_img[i][j],  r+1)

        img = next_img
    
    return get_lit_pxl_count(img)
            

print(main())