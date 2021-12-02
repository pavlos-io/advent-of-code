from collections import defaultdict, OrderedDict

foods = [l.strip().strip(")") for l in open('input.txt').readlines()]

#common
d     = {}
count = defaultdict(int)
all_ingridients = set()

for food in foods:
  ingridients, allergens = food.split(" (contains ")
  ingridients            = set(ingridients.split(' '))
  all_ingridients.update(ingridients)

  for ingridient in ingridients:
    count[ingridient] += 1

  for allergen in allergens.split(', '):
    if(al := d.get(allergen)) is None:
      d[allergen] = ingridients
    else:
      d[allergen] = al.intersection(ingridients)

#pt1
contain_allergens = set.union(*d.values())

out = sum( count[ingrt] for ingrt in (all_ingridients - contain_allergens) )

print('part 1:', out)

#pt2
while any( [len(v) > 1 for k, v in d.items()] ):
  for allergen, ingridients in d.items():
    if len(ingridients) == 1:
      for k, v in d.items():
        if k == allergen:
          continue
        d[k] = v - ingridients

d   = OrderedDict(sorted(d.items()))
out = ','.join( [list(v)[0] for k,v in d.items()] )
print('part 2:', out) 

