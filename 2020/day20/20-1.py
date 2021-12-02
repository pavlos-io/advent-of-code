tiles = open("input.txt").read().split("\n\n")
tiles = { int(tile.split("\n")[0].split(" ")[1][:-1]): tile.split("\n")[1:] for tile in tiles }

def get_borders(tile):
  borders = []
  borders.append(tile[0])
  borders.append(tile[-1])
  borders.append(get_column(tile, 0))
  borders.append(get_column(tile, -1))
  return borders

def get_column(m, i):
  return ''.join([row[i] for row in m])

def count_matching_sides(tile1, tile2):
  counter = 0
  for border1 in borders[tile1]:
    for border2 in borders[tile2]:
      if border1 == border2 or border1 == border2[::-1]:
        counter += 1
  return counter

borders = {}
matches = {}

for k, v in tiles.items():
  borders[k] = get_borders(v)

for tile_num, tile in tiles.items():
  for k, v in tiles.items():
    if k == tile_num:
      continue

    count = matches.get(tile_num, 0)
    matches[tile_num] = count + count_matching_sides(tile_num, k)

out = 1
for k, v in matches.items():
  if v == 2:
    out *= k
print(matches)