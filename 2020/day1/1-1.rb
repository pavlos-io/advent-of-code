input  = File.readlines('input.txt').map(&:to_i)
target = 2020

def two_sum arr, target
  complements = {}
  arr.each_with_index do |el, idx|
    if complements[el]
      return el, arr[ complements[el] ]
    end
    complements[target - el] = idx
  end
end

addends = two_sum(input, target)
puts addends.inject(:*)