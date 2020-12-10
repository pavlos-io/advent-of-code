input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '').to_i
}.sort

prev = 0
h = {
  1 => 0,
  2 => 0,
  3 => 0
}

input.each do |num|
  h[num-prev] += 1
  prev = num
end

puts h[1]*(h[3]+1)



