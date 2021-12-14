from collections import defaultdict, Counter

with open('input.txt', 'r') as f:
    tmpl, insertions = f.read().split('\n\n')
    insertions = dict([el.split(' -> ') for el in insertions.split('\n')])


def main(steps):
    pairs = defaultdict(int)
    freq  = Counter(tmpl)
    
    for i in range(1, len(tmpl)):
        pairs[(tmpl[i-1], tmpl[i])] += 1

    for _ in range(steps):
        d = defaultdict(int)
        for (a, b), count in pairs.items():
            c = insertions[a + b]
            d[(a, c)] += count
            d[(c, b)] += count
            freq[c] += count
        pairs = d

    return max(freq.values()) - min(freq.values())


print(main(10), main(40))