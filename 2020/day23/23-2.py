from ring import Ring

inp = [int(l.strip()) for l in open('input.txt').read()]

for i in range(max(inp)+1, 1000001):
  inp.append(i)

r       = Ring(inp)
curr    = r.find(inp[0])
inp_min = min(inp)

for i in range(10000000):
  tmp  = r.remove(curr.nxt.val, 2)

  destination_val = curr.val - 1
  while not r.has(destination_val):
    destination_val -= 1
    if destination_val < inp_min:
      destination_val = r.get_max_val()
      break
  r.insert(destination_val, tmp)
  curr = curr.nxt

one = r.find(1)
print(one.nxt.val * one.nxt.nxt.val)