class Ring:
  
  class Node:
    def __init__(self, val, prev=None, nxt=None):
      self.val  = val
      self.nxt  = nxt
      self.prev = prev

  m = {}
  def __init__(self, items):
    first, *_ = items
    prev = None

    for item in items:
      node = self.Node(item)
      self.m[item] = node
      if prev:
        node.prev = prev
        prev.nxt  = node
      prev = node

    self.m[first].prev = prev
    prev.nxt           = self.m[first]

  def remove(self, val, rng=0):
    node = self.m[val]
    prev = node.prev
    node.prev = None
    self.m.pop(node.val)

    curr = node.nxt
    for i in range(rng):
      self.m.pop(curr.val)
      curr = curr.nxt
    
    curr     = curr.prev
    prev.nxt = curr.nxt
    curr.nxt.prev = prev
    curr.nxt = None
    return node

  def insert(self, after, chain):
    node = self.find(after)
    nxt  = node.nxt
    node.nxt   = chain
    chain.prev = node

    curr = chain
    while curr:
      self.m[curr.val] = curr
      if not curr.nxt:
        break
      curr = curr.nxt

    curr.nxt = nxt
    nxt.prev = curr

  def has(self, val):
    return val in self.m

  def find(self, val):
    if not self.has(val):
      return None
    return self.m[val]

  def get_max_val(self):
    return max(self.m.keys())

  def traverse(self, start):
    if not self.has(start):
      return ''

    out  = [start]
    node = self.m[start].nxt

    while node and node.val != start:
      out.append(node.val)
      node = node.nxt

    return out

  def create_node(self, val):
    return self.Node(val)

