require_relative "calc"

input = File.read("input.txt").split("\n").map{ |el|
  el = el.gsub(' ', '')

  # Adds parenthesis around '+' expressions s.t. '+' has higher precedence.
  counter = 0
  while counter < el.count('+') do
    plus_indices = el.split('').each_index.select{ |i| el[i] == '+' }
    plus_idx = plus_indices[counter]
    left, right = plus_idx-1, plus_idx+1

    if el[left] == ')'
      stack = [')']
      while !stack.empty? do
        left -= 1
        if el[left] == ')'
          stack << ')'
        elsif el[left] == '('
          stack.pop
        end
      end
    end

    if el[right] == '('
      stack = ['(']
      while !stack.empty? do
        right += 1
        if el[right] == '('
          stack << '('
        elsif el[right] == ')'
          stack.pop
        end
      end
    end

    el.insert(right+1, ')')
    el.insert(left, '(')

    counter += 1
  end
  el
}

total = 0
input.each do |problem|
  res, i = Calc.compute 0, problem
  total += res
end

p total