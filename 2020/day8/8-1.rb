input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
}

seen = {}
idx = acc = 0


while (seen[idx].nil?) do
  seen[idx] = true
  
  line    = input[idx].split(' ')
  command = line[0]
  val     = line[1].to_i

  case command  
  when "acc"
    acc += val
    idx += 1
  when "jmp"
    idx += val
  else
    idx += 1
  end
end

puts acc

