from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]
    print(lines)

gamma, eps = "", ""
gte_ones_in_col = {}

for col in range(len(lines[0])):
    count = defaultdict(int)
    for row in range(len(lines)):
        count[lines[row][col]] += 1

    # gte_ones_in_col[col] = (count['1'] > count['0'], count['1'] == count['0'])

    gamma += '0' if count['0'] > count['1'] else '1'
    eps += '0' if count['0'] < count['1'] else '1'

gamma = int(gamma, 2)
eps = int(eps, 2)

curr_set1 = set(lines)
ans1 = None

for col in range(len(lines[0])):
    if ans1:
        break
    count = defaultdict(int)
    for row in range(len(lines)):
        if lines[row] not in curr_set1:
            continue
        count[lines[row][col]] += 1
    
    gte = '1' if count['1'] >= count['0'] else '0'
    for el in list(curr_set1):
        if el[col] != gte:
           curr_set1.remove(el)
           if len(curr_set1) == 1:
               ans1 = list(curr_set1)[0]
               break

curr_set2 = set(lines)
ans2 = None

for col in range(len(lines[0])):
    if ans2:
        break
    count = defaultdict(int)
    for row in range(len(lines)):
        if lines[row] not in curr_set2:
            continue
        count[lines[row][col]] += 1

    gte = '0' if count['0'] <= count['1'] else '1'
    for el in list(curr_set2):
        if el[col] != gte:
           curr_set2.remove(el)
           if len(curr_set2) == 1:
               ans2 = list(curr_set2)[0]
               break

print(int(ans1, 2) * int(ans2, 2))


# print(gamma * eps)
p1, p2 = 0, 0
