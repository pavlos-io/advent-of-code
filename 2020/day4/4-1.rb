input = File.read("input.txt").split(/\n{2,}/).map{ |el| 
  el.split(" ").map{ |entry| entry.split(":") }.to_h
}

fields = [ "byr", "iyr", "eyr","hgt", "hcl", "ecl", "pid" ]

puts input.count { |p|
  fields.all? { |f| p[f] }
}