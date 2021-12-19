import math
from itertools import combinations

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()


def parse_int(line, idx):
    start = idx
    num = 0
    while idx < len(line) and line[idx].isdigit():
        num = num * 10 + int(line[idx])
        idx += 1

    return num, idx - start


def replace(line, l, r, new_val):
    return line[:l] + str(new_val) + line[r+1:]

# Can be used instead of eval

# def line_to_list(line, idx=0):
#     if line[idx].isdigit():
#         return parse_int(line, idx)[0]

#     if line[idx + 1] != '[':
#         d, d_len = parse_int(line, idx + 1)
#         return [
#             d,
#             line_to_list(line, idx + d_len + 2)
#         ]
#     else:
#         next_idx = idx + 1
#         open = 1
#         while open:
#             next_idx += 1
#             if line[next_idx] == ']':
#                 open -=1
#             elif line[next_idx] == '[':
#                 open += 1
        
#         return [
#             line_to_list(line, idx + 1),
#             line_to_list(line, next_idx + 2)
#         ]


def will_explode(line):
    idx, open = 0, 0

    while idx < len(line) and open < 5:
        if line[idx] == '[':
            open += 1
        elif line[idx] == ']':
            open -= 1

        idx += 1
    
    return open == 5


def will_split(line):
    idx = 0
    while idx < len(line):
        if line[idx].isdigit():
            num, num_len = parse_int(line, idx)
            idx += num_len
            if num > 9:
                return True
        idx += 1
    
    return False


def get_explode_bounds(line):
    idx, open = 0, 0
    l, r = -1, -1

    while idx < len(line):
        if line[idx] == '[':
            open += 1
        elif line[idx] == ']':
            open -= 1

        if open == 5:
            l = idx
            while line[idx] != ']':
                idx += 1
            r = idx
            break

        idx += 1
    
    return l, r
    

def get_left_right_indices(line, left_bound, right_bound):
    left_idx, right_idx = None, None
    idx = 0

    while idx < left_bound:
        if line[idx].isdigit():
            _, d_len = parse_int(line, idx)
            left_idx = idx
            idx += d_len - 1
        idx += 1

    idx = right_bound
    while idx < len(line):
        if line[idx].isdigit():
            right_idx = idx
            break
        idx += 1

    return left_idx, right_idx
    

def explode_left(line, left_bound, right_bound, val):
    left_idx, _ = get_left_right_indices(line, left_bound, right_bound)

    if left_idx:
        left_num, ln = parse_int(line, left_idx)
        new_left = left_num + val
        line = replace(line, left_idx, left_idx + ln - 1, new_left)

    return line


def explode_right(line, left_bound, right_bound, val):
    _, right_idx = get_left_right_indices(line, left_bound, right_bound)

    if right_idx:
        right_num, ln = parse_int(line, right_idx)
        new_right = right_num + val
        line = replace(line, right_idx, right_idx + ln - 1, new_right)

    return line


def explode(line):
    l, r = get_explode_bounds(line)
    a, b = list(map(int, line[l + 1:r].split(',')))
    line = explode_left(line, l, r, a)
    
    #recalc bounds since left explode might have changed the line len!
    l, r = get_explode_bounds(line)
    line = explode_right(line, l, r, b)
    
    l, r = get_explode_bounds(line)

    return replace(line, l, r, 0)


def split(line):
    idx = 0
    l = -1
    while idx < len(line):
        if line[idx].isdigit():
            l = idx
            num, num_len = parse_int(line, idx)
            idx += num_len
            if num > 9:
                fl, cl = num//2, math.ceil(num/2)
                return replace(line, l, idx - 1, f'[{fl},{cl}]')
        idx += 1
    return line


def get_magnitude(num):
    if isinstance(num, int):
        return num

    return 3 * get_magnitude(num[0]) + 2 * get_magnitude(num[1])


def add(a, b):
    a = f'[{a},{b}]'
    while will_explode(a) or will_split(a):
        
        if will_explode(a):
            a = explode(a)
            continue

        if will_split(a):
            a = split(a)
    
    return a


def main():
    line = lines[0]
    for i in range(1, len(lines)):
        line = add(line, lines[i])
    
    max_mag = 0
    for a, b in combinations(lines, 2):
        max_mag = max(max_mag, get_magnitude(eval(add(a, b))))
        max_mag = max(max_mag, get_magnitude(eval(add(b, a))))

    return get_magnitude(eval(line)), max_mag


print(main())