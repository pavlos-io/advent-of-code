input = File.readlines('input.txt').map{|el| el.gsub(/\n/, "")}

i = j = tree_counter = 0
m = input.size - 1
n = input[0].size

while (i < m) do
  j = (j+3) % n
  i += 1
  tree_counter += 1 if input[i][j] == "#"
end

puts tree_counter
