from collections import defaultdict
from itertools import permutations

with open('input.txt', 'r') as f:
    scanners = []
    lines = f.read().split('\n\n')
    for line in lines:
        _, *pts = line.split('\n')
        beacons = [list(map(int, pt.split(','))) for pt in pts]
        scanners.append(beacons)


def get_scanner_pos_if_overlap(beacons, other_beacons, threshold=3):
    for p in permutations(other_beacons):
        overlaps = defaultdict(int)
        for (x1, y1), (x2, y2) in zip(beacons, p):
            overlaps[(x1 - x2), (y1 - y2)] += 1
        
        for k, v in overlaps.items():
            if v >= threshold:
                return True, k

    return False, None


def main():
    done    = set([0])
    scanner = 0

    scanner_pos    = [None] * len(scanners)
    scanner_pos[0] = (0, 0)
    
    while len(done) < len(scanners):
        for other_scanner, beacons in enumerate(scanners):
            if other_scanner in done:
                continue

            overlap, pos = get_scanner_pos_if_overlap(
                scanners[scanner], 
                scanners[other_scanner]
            )
            
            if overlap:
                scanner_pos[other_scanner] = pos
                scanner = other_scanner
                done.add(other_scanner)
                break

    return scanner_pos


a = [-618, -824, -621]
b = [686, 422, 578]

for i, p in enumerate(permutations(b)):
    x1, y1, z1 = a
    x2, y2, z2 = p
    print('  ', (x1 - x2), (y1 - y2), (z1 - z2))


# print(main())