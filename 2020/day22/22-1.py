from collections import deque

with open('input.txt') as f:
  my_deck, other_deck = list(map(lambda l: l.split("\n"), f.read().split("\n\n")))

my_deck.pop(0)
other_deck.pop(0)

# right is bottom of the deck
my_deck    = deque( list(map(int, my_deck)) )
other_deck = deque( list(map(int, other_deck)) )

while len(my_deck) and len(other_deck):
  my, other = my_deck.popleft(), other_deck.popleft()
  
  if my > other:
    my_deck.append(my)
    my_deck.append(other)
  else:
    other_deck.append(other)
    other_deck.append(my)

final_deck    = my_deck if len(my_deck) else other_deck
winning_score = 0
for i in range ( 1, len(final_deck) + 1 ):
  winning_score += i*final_deck.pop()

print(winning_score)