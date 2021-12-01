input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '').to_i
}

target = 1721308972
l      = 0
r      = 1
sum    = input[l] + input[r]

while sum != target do #sliding window
  if sum < target
    r += 1
    sum += input[r]
  else
    sum -= input[l]
    l += 1
  end
end

window = input[l, r-l+1]
puts window.min + window.max

# 209694133