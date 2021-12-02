from ring import Ring

inp = [int(l.strip()) for l in open('input.txt').read()]

r       = Ring(inp)
curr    = r.find(inp[0])
inp_min = min(inp)

for i in range(100):
  tmp  = r.remove(curr.nxt.val, 2)

  destination_val = curr.val - 1
  while not r.has(destination_val):
    destination_val -= 1
    if destination_val < inp_min:
      destination_val = r.get_max_val()
      break
  r.insert(destination_val, tmp)
  curr = curr.nxt

print( ''.join( list(map(str, r.traverse(1)))[1:] ) )