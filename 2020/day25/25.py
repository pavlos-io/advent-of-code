card_pub, door_pub = [int(line.strip()) for line in open('input.txt').readlines()]

P = 20201227

def get_loop_size(public_key):
  val         = 1
  subject_num = 7
  loop_size   = 0

  while val != public_key:
    val = (val*subject_num) % P
    loop_size += 1
  
  return loop_size

def get_encryption_key(subject_num, loop_size):
  val = 1
  for i in range(1, loop_size+1):
    val = (val*subject_num) % P
  return val

card_loop = get_loop_size(card_pub)
door_loop = get_loop_size(door_pub)
print( get_encryption_key(door_pub, card_loop), get_encryption_key(card_pub, door_loop) )