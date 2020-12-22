from collections import deque

with open('input.txt') as f:
  my_deck, other_deck = list(map(lambda l: l.split("\n"), f.read().split("\n\n")))

my_deck.pop(0)
other_deck.pop(0)

# right is bottom of the deck
my_deck    = deque( list(map(int, my_deck)) )
other_deck = deque( list(map(int, other_deck)) )

def start_game(deck1, deck2):
  history = []

  while len(deck1) and len(deck2):
    for d1, d2 in history:
      if deck1 == d1 and deck2 == d2:
        return 1

    history.append( (deck1.copy(), deck2.copy()) )
    hand1, hand2 = deck1.popleft(), deck2.popleft()
    
    if len(deck1) >= hand1 and len(deck2) >= hand2:
      if start_game(copy_deck(deck1, hand1), copy_deck(deck2, hand2)):
        end_round(deck1, hand1, hand2)
      else:
        end_round(deck2, hand2, hand1)
    else:
      if hand1 > hand2:
        end_round(deck1, hand1, hand2)
      else:
        end_round(deck2, hand2, hand1)

  return 1 if len(deck1) else 0

def copy_deck(deck, num):
  if len(deck) < num:
    return None

  cp = deck.copy()
  while len(cp) > num:
    cp.pop()
  return cp

def end_round(deck, hand1, hand2):
  deck.append(hand1)
  deck.append(hand2)

final_deck    = my_deck if start_game(my_deck, other_deck) else other_deck
winning_score = 0
for i in range ( 1, len(final_deck) + 1 ):
  winning_score += i*final_deck.pop()

print(winning_score)