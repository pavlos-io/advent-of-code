input = File.read("input.txt").split(/\n{2,}/).map{ |el| 
  el.split(" ").map{ |entry| entry.split(":") }.to_h
}

fields = { 
  "byr" => /^19[2-9][0-9]|200[0-2]$/,
  "iyr" => /^20(1[0-9]|20)$/,
  "eyr" => /^20(2[0-9]|30)$/,
  "hgt" => /^1([5-8][0-9]|9[0-3])cm|59|6[0-9]|7[0-6]in$/,
  "hcl" => /^#[0-9a-f]{6}$/,
  "ecl" => /^amb|blu|brn|gry|grn|hzl|oth$/,
  "pid" => /^\d{9}$/ 
}

puts input.count { |p|
  fields.all? { |type, regexp| p[type] && p[type].match?(regexp) }
}