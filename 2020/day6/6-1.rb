input = File.read("input.txt").split("\n\n")

counter = 0

input.each do |groups|
  
  questions = {}
  groups    = groups.split("\n")

  groups.each do |group|
    group.split('').each do |q|
      questions[q] = true
    end
  end
  
  counter += questions.length
end

puts counter