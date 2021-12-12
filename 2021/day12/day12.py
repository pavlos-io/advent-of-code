from collections import defaultdict

START = 'start'
END   = 'end'

with open('input.txt', 'r') as f:
    adj_list = defaultdict(list)
    for line in f.read().splitlines():
        a, b = line.split('-')
        
        adj_list[a].append(b)

        if a != START and b != END:
            adj_list[b].append(a)


def is_small_cave(node):
    return node.lower() == node


def dfs(node, small_seen, allowed_small=None, allowed_counter=0):
    if node == END:
        return 1
    
    if node in small_seen:
        return 0

    if node == allowed_small:
        if allowed_counter >= 2:
            return 0
    elif is_small_cave(node):
        small_seen.add(node)

    paths = 0
    for child in adj_list[node]:
        # Important to notice: No two big caves are adjecent. 
        # If there were such two nodes, an inf. cycle would occur!

        paths += dfs(
            child, 
            small_seen.copy(), 
            allowed_small=allowed_small,
            allowed_counter=allowed_counter + 1 if node == allowed_small else allowed_counter
        )

    return paths


def main():
    p1, p2 = 0, 0

    p1 = dfs(START, set())

    small_caves = set([c for c in adj_list.keys() 
        if is_small_cave(c) and c not in [START, END]
    ])

    p2 = p1
    for sc in small_caves:
        p2 += dfs(START, set(), allowed_small=sc) - p1
    
    return p1, p2

print(main())