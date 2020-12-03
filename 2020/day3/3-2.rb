input = File.readlines('input.txt').map{|el| el.gsub(/\n/, "")}

def count_trees(input, x_step, y_step)
  m = input.size 
  n = input[0].size
  i = j = tree_counter = 0

  while (i < m - y_step)
    j = (j + x_step) % n
    i += y_step
    tree_counter += 1 if input[i][j] == "#"
  end

  tree_counter
end

trials = [
  [1, 1],
  [3, 1],
  [5, 1],
  [7, 1],
  [1, 2]
]

trees_per_trial = []
trials.each do |trial|
  trees_per_trial << count_trees(input, trial[0], trial[1])
end

puts trees_per_trial.inject(:*)