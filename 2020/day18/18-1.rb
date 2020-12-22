require_relative "calc"

input = File.read("input.txt").split("\n").map{ |el|
  el.gsub(' ', '')
}

total = 0
input.each do |problem|
  res, i = Calc.compute 0, problem
  total += res
end

p total