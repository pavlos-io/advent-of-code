import sys
from collections import Counter

with open('input.txt', 'r') as f:
    nums = list(map(int, f.read().split(',')))
    freq = Counter(nums)

def p1_fuel_cost(a, b):
    return abs(a - b)

def p2_fuel_cost(a, b):
    """
    Each step increases fuel cost by 1 => 1 + 2 + ... + n, where n = |a-b|.
    This is just a series from 1 to n of x, which equal (n(n+1))/2.
    """
    n = abs(a - b)
    return (n * (n + 1))//2

def main(fuel_cost):
    global nums

    nums = list(set(nums))
    min_moves = sys.maxsize

    for a in range(max(nums)):
        moves = 0
        for b in nums:
            moves += fuel_cost(a, b) * freq[b]
        min_moves = min(min_moves, moves)

    return min_moves


print(main(p1_fuel_cost), main(p2_fuel_cost))
