require 'Matrix'

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

nearby_tickets = nearby_tickets.reject { |ticket|
  ticket.any?{ |n| field_rules.none? { |k,v| valid?(n, *v) } }
}

m     = Matrix[ *nearby_tickets ]
keys  = field_rules.keys
order = Array.new(keys.count, '')
out   = 1
overlap = {}

(0..keys.count-1).each do |i|
  col        = m.column(i).to_a
  overlap[i] = []

  keys.each do |field|
    overlap[i] << field if col.all? { |n| valid?(n, *field_rules[field]) }
  end
end

(0..keys.count-1).each do |i|
  u_field      = overlap.select { |k,v| v.size==1 }
  u_col        = u_field.keys.first
  u_field_name = u_field.values.first.first
  order[u_col] = u_field_name
 
  overlap.each { |col, matches|
    overlap[col] = matches.reject{ |el| el == u_field_name }
  }
end

indices = order.each_index.select{|i| order[i].include? "departure"}
indices.each { |idx| out *= my_ticket[idx] }
p out
