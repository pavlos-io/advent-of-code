import operator, re
from collections import defaultdict
from queue import Queue

inp = [re.findall('e|se|sw|w|nw|ne', l.strip()) for l in open('input.txt').readlines()]

m = {
  'e': (1,0),
  'w': (-1,0),
  'sw': (-0.5,-0.5),
  'se': (0.5,-0.5),
  'nw': (-0.5,0.5),
  'ne': (0.5,0.5)
}

dirs  = list(m.values())
tiles = defaultdict(bool) #default is false and true => black

for l in inp:
  curr = (0, 0)
  for instruction in l:
    curr = tuple(map(operator.add, curr, m[instruction]))
  tiles[curr] = not tiles[curr]

print( 'part1', list(tiles.values()).count(True) )

def bfs(tiles):
  cp   = tiles.copy()
  q    = Queue()
  seen = set()

  for k, v in tiles.items():
    q.put((k, True))
    seen.add(k)

  while not q.empty():
    parent, ok = q.get()
    process_tile(parent, tiles, cp) 

    if ok:
      for adj in dirs:
        tile = tuple(map(operator.add, parent, adj))
        if tile not in seen:
          q.put((tile, False))
          seen.add(tile)
  return cp

def process_tile(tile, tiles, cp):
  black = 0
  for adj in dirs:
    curr = tuple(map(operator.add, tile, adj))
    if curr in tiles:
      black += tiles[curr] == True
  
  if tiles[tile] and (black == 0 or black > 2):
    cp[tile] = False
  else: #new tiles or white tiles
    if black == 2:
      cp[tile] = True

  return cp

for i in range(100):
  tiles = bfs(tiles)

print( 'part2', list(tiles.values()).count(True) )