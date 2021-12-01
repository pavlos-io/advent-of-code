input = File.read("input.txt").split(',').map(&:to_i)

when_said = {}

input.each_with_index do |num, idx|
  when_said[num] = idx+1
end

last = 0
turn = input.size + 2

while turn <= 2020 do
  
  if when_said[last]
    new_num = (turn-1) - when_said[last]
  else
    new_num = 0
  end

  when_said[last] = turn - 1
  last = new_num
  turn += 1
end

p last