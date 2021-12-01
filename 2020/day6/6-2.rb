input = File.read("input.txt").split("\n\n")

counter = 0

input.each do |groups|
  
  questions  = {}
  groups     = groups.split("\n")
  group_size = groups.count
  
  groups.each do |group|
    group.split('').each do |q|
      if questions[q]  
        questions[q] += 1
      else
        questions[q] = 1
      end
    end
  end
  
  questions.each do |k,v|
    counter += 1 if v == group_size
  end
end

puts counter