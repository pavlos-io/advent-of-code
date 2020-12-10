input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '').to_i
}.push(0).sort

dp    = Array.new(input.count+1, 0)
dp[0] = 1
i     = 1

while i < input.count do
  j = 1
  while (i-j >= 0) && (input[i] - input[i-j] <= 3) do
    dp[i] += dp[i-j]
    j+=1
  end

  i+=1
end

puts dp[input.count-1]
