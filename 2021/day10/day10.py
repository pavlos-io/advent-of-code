with open('input.txt', 'r') as f:
    lines = [l.replace('\n', '') for l in f.readlines()]


corruption_scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

completion_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

pairs = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}


def main():
    p1, p2 = 0, 0
    corruption_points = []
    completion_points = []

    for line in lines:
        stack = []
        corrupt = False

        for c in line:
            if c in pairs:
                if len(stack) and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    corruption_points.append(corruption_scores[c])
                    corrupt = True
                    break
            else:
                stack.append(c)
        
        if not corrupt:
            score = 0
            while stack:
                c = stack.pop()
                score *= 5
                score += completion_scores[c]
            
            completion_points.append(score)


    p1 = sum(corruption_points)

    completion_points.sort()
    p2 = completion_points[(len(completion_points) - 1)//2]

    return p1, p2


print(main())