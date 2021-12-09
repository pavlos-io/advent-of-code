from collections import Counter

signals, outputs = [], []

nums = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}

easy_nums = [1, 4, 7, 8]

num_to_letter = {
    1: ['c', 'f'],
    4: ['b', 'd'],
    7: ['a'],
    8: ['e', 'g'],
}

seg_len_to_i = {
    2: 1,
    4: 4,
    3: 7,
    7: 8
}

i_to_seg_len = {
    1: 2,
    4: 4,
    7: 3,
    8: 7
}

digit_counter = Counter()


def parse_digit(s):
    return "".join(s)

def parse_digits(ds):
    return [parse_digit(s) for s in ds.split(' ')]


# def parse_digits_to_i(ds):
#     return [nums.get(d) for d in parse_digits(ds)]

items = []

with open('input.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        s, o = l.replace('\n', '').split(' | ')
        items.append((
            parse_digits(s),
            parse_digits(o), 
            Counter([seg_len_to_i.get(len(d)) for d in parse_digits(s)])
        ))

def get_map():
    return {
    'a': None,
    'b': None,
    'c': None,
    'd': None,
    'e': None,
    'f': None,
    'g': None,
}


potential_maps = []

def _f(digits, num_idx, mmap, seen):
    if num_idx == len(easy_nums):
        if all(mmap.values()):
            potential_maps.append(mmap)
        return

    s = None
    num = easy_nums[num_idx]
    for d in digits:
        if len(d) == i_to_seg_len[num]:
            s = d
            break

    s = [l for l in s if l not in seen]

    d = mmap.copy()
    sseen = seen.copy()
    for l1, l2 in zip(s, num_to_letter[num]):
        sseen.add(l1)
        d[l1] = l2
        _f(digits, num_idx+1, d, sseen)

    d = mmap.copy()
    sseen = seen.copy()
    for l1, l2 in zip(s[::-1], num_to_letter[num]):
        sseen.add(l1)
        d[l1] = l2
        _f(digits, num_idx+1, d, sseen)

def transform(digit, maping):
    s = ""
    for l in digit:
        s += maping[l]
    return s

def get_num(s):
    return nums.get("".join(sorted(s)))


def get_correct_config(digits):
    for idx, maping in enumerate(potential_maps):
        num_set = set()
        for digit in digits:
            actual_s = transform(digit, maping)

            actual_d = get_num(actual_s)
            if actual_d is not None:
                num_set.add(actual_d)

        if len(num_set) == len(digits):
            return maping


def get_config(digits):
    _f(digits, 0, get_map(), set())
    return get_correct_config(digits)


def main(targets):
    ans = 0
    p2 = 0
    for digits, output, counter in items:
        conf = get_config(digits)
        output_num = ""
        for o in output:
            if len(o) in seg_len_to_i:
                ans += counter[seg_len_to_i[len(o)]]

            output_num += str(get_num(transform(o, conf)))
        p2 += int(output_num)

    return ans, p2

print(main(set([1, 4, 7, 8])))
# print(main(p1_fuel_cost), main(p2_fuel_cost))
