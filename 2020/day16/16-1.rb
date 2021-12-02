input = File.read("input.txt").split("\n\n")

field_rules = input[0].split("\n").map { |el|
  field, rules = el.split(':').map(&:strip)
  rules = rules.split(" or ").map{ |el| el.split("-") }.flatten.map(&:to_i)
  [field, rules]
}.to_h

my_ticket = input[1].split("\n")[1].split(',').map(&:to_i)

nearby_tickets = input[2].split("\n")[1..-1].map { |el| 
  el.split(",").map(&:to_i)
}

def valid? num, a, b, c, d
  (a <= num && num <= b) || (c <= num && num <= d)
end

errors = []

nearby_tickets.each do |ticket|
  errors.concat ticket.select{ |n| field_rules.none? { |k,v| valid?(n, *v) } }
end

p errors.sum