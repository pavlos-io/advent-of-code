input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '').to_i
}

def is_sum? input, left, right
  complements = {}
  target      = input[right]

  while left < right do
    el = input[left]
    
    return true if complements[el]
    
    complements[target - el] = left
    left += 1
  end
  
  return false
end

l  = 0
r  = 25

while true do
  if is_sum?(input, l, r)
    l += 1
    r += 1
  else
    puts input[r]
    break
  end
end


