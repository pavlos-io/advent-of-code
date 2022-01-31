from collections import defaultdict
from itertools import permutations
from types import new_class

# with open('input.txt', 'r') as f:
#     algo, img = f.read().split('\n\n')
#     img = [row for row in img.split('\n')]

player_pos   = [2, 1]
player_score = [0, 0]

def p1():
    die, player  = 0, 0
    rounds = 0

    while not [1 for score in player_score if score >= 1000]:
        a, b, c = die + 1, die + 2, die + 3

        player_pos[player] += (a + b + c) % 10
        if player_pos[player] > 10:
            player_pos[player] %= 10
        player_score[player] += player_pos[player]

        die += 3
        die %= 1000
        if die == 0:
            die = 1
        
        player = 1 - player
        rounds += 3

    losing_score = player_score[player]
    return losing_score * rounds

def get_pos_score(player, roll, player_pos, player_score):
    player_pos[player] += roll
    if player_pos[player] > 10:
        player_pos[player] %= 10
    player_score[player] += player_pos[player]

    return player_pos, player_score

uni_score = {
    0: 0,
    1: 0
}

memo = {
    0: {
        1: defaultdict(int),
        2: defaultdict(int),
        3: defaultdict(int),
    },
    1: {
        1: defaultdict(int),
        2: defaultdict(int),
        3: defaultdict(int),
    }
}

def p2(player, roll, pos, score):
    if score[player] >= 21:
        return player
    
    try:
        return memo[player][roll][pos][score]
    except KeyError:
        pass

    if roll >= 3:
        player = 1 - player
        roll = 0
    
    p, scr = get_pos_score(player, 1, pos, score)
    w = memo[player][1][(p[player], scr[player])] = p2(player, roll + 1, p, scr)
    uni_score[w] += 1

    p, scr = get_pos_score(player, 2, pos, score)
    w = memo[player][2][(p[player], scr[player])] = p2(player, roll + 1, p, scr)
    uni_score[w] += 1

    p, scr = get_pos_score(player, 3, pos, score)
    w = memo[player][3][(p[player], scr[player])] = p2(player, roll + 1, p, scr)
    uni_score[w] += 1



def main():


            

print(main())