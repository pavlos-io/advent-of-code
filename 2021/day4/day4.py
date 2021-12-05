from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = f.read().split('\n')
    nums = [n for n in lines[0].split(',')]
    rest = [l.strip().replace('  ', ' ').split(' ') for l in lines[1:] if l]
    boards = []
    for i in range(5, len(rest) + 1, 5):
        boards.append(rest[i-5:i])

MARK = '*'

num_idx       = 0
winner_boards = []
board_state   = defaultdict(lambda: {
    'rows': defaultdict(int),
    'cols': defaultdict(int)
})

def mark_boards(num):
    for idx, board in enumerate(boards):
        if idx in winner_boards:
            continue
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == num:
                    board[i][j] = MARK
                    board_state[idx]['rows'][i] += 1
                    board_state[idx]['cols'][j] += 1
                    
        if any([v == len(board[0]) for v in board_state[idx]['rows'].values()])\
            or any([v == len(board) for v in board_state[idx]['cols'].values()]):
            winner_boards.append(idx)


def get_board_sum(idx):
    s = 0
    for row in boards[idx]:
        for el in row:
            if el != MARK:
                s += int(el)
    return s


p1 = None
while len(winner_boards) < len(boards):
    num = nums[num_idx]
    mark_boards(num)
    if len(winner_boards) == 1 and not p1:
        p1 = get_board_sum(winner_boards[0]) * int(num)
    num_idx += 1

p2 = get_board_sum(winner_boards[-1]) * int(nums[num_idx-1])
print(p1, p2)
