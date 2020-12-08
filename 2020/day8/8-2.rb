input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
  line = line.split(' ')
  [ line[0], line[1].to_i ]
}

def execute input, idx, acc, seen, can_change
  return [true, acc]  if idx >= input.count
  return [false, acc] if seen[idx]

  seen[idx] = true
  
  command, val = input[idx]

  case command  
  when "acc"
    return execute(input, idx+1, acc+val, seen, can_change)
  when "jmp"
    jmp = execute(input, idx+val, acc, seen, can_change)  
    return jmp if jmp[0]
    
    return execute(input, idx+1, acc, seen, !can_change) if can_change
  else
    nop = execute(input, idx+1, acc, seen, can_change)  
    return nop if nop[0]

    return execute(input, idx+val, acc, seen, !can_change) if can_change
  end

  return [false, -1]
end


puts execute(input, 0, 0, {}, true)

