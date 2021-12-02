with open('input.txt', 'r') as f:
    nums = [int(l.replace('\n', '')) for l in f.readlines()]

p1 = p2 = 0

for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        p1 += 1

for i in range(1, len(nums) - 2):
    prev = nums[i-1] + nums[i] + nums[i+1]
    curr = nums[i] + nums[i+1] + nums[i+2]
    if curr > prev:
        p2 += 1

print(p1, p2)
