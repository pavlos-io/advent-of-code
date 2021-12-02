with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '').split(' ') for l in f.readlines()]
    commands = [(l[0], int(l[1])) for l in lines]

p1, p2 = [0, 0], [0, 0]  # [horiz, depth]
aim = 0

for direction, val in commands:
    if direction == 'forward':
        p1[0] += val
        p2[0] += val
        p2[1] += aim * val
    elif direction == 'down':
        p1[1] += val
        aim += val
    elif direction == 'up':
        p1[1] -= val
        aim -= val

print(p1[0] * p1[1], p2[0] * p2[1])
