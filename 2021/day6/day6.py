from collections import defaultdict

with open('input.txt', 'r') as f:
    nums = list(map(int, f.read().split(',')))

CYCLE = 7

def main(days):
    fish_count = len(nums)

    fish_count_in_days_left = {k: 0 for k in range(9)}
    for n in nums:
        fish_count_in_days_left[n] += 1

    for d in range(days):
        new_state = {k: 0 for k in range(9)}
        for days_left, count in fish_count_in_days_left.items():
            if not count:
                continue
            
            new_day = days_left-1 if days_left > CYCLE else (days_left - 1) % CYCLE
            new_state[new_day] += count
            if days_left == 0:
                new_state[8] = count
                fish_count += count
        
        for k, v in new_state.items():
            fish_count_in_days_left[k] = v

    return sum((fish_count_in_days_left.values()))

print(main(80), main(256))
