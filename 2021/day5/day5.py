from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    segments = [l.split(' -> ') for l in lines]


def get_y_coordinate(x1, y1, x2, y2, x):
    m = (y2 - y1) / (x2 - x1)
    y = m*x - m*x1 + y1
    return int(y)


def get_pts_on_vertical_line(x, y1, y2):
    if y2 < y1:
        return get_pts_on_vertical_line(x, y2, y1)
        
    pts = []
    while(y1 <= y2):
        pts.append((x, y1))
        y1 += 1
    
    return pts

def get_pts_on_line(x1, y1, x2, y2):
    if x2 < x1:
        return get_pts_on_line(x2, y2, x1, y1)
    elif x1 == x2:
        return get_pts_on_vertical_line(x1, y1, y2)
    
    pts = []
    x = x1
    while x <= x2:
        pts.append((x, get_y_coordinate(x1, y1, x2, y2, x)))
        x += 1
    
    return pts


def get_overlap_count(without_diag=True):
    pt_count = defaultdict(int)
    for seg in segments:
        start, end = seg[0], seg[1]
        x1, y1 = map(int, start.split(','))
        x2, y2 = map(int, end.split(','))
        
        if without_diag and (x1 != x2) and (y1 != y2):
            continue

        pts = get_pts_on_line(x1, y1, x2, y2)
        for pt in pts:
            pt_count[pt] += 1

    return sum( [c >= 2 for c in pt_count.values()] )


print(get_overlap_count(), get_overlap_count(without_diag=False))

