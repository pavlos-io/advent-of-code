passes = File.read("input.txt").split("\n").map{ |el| 
  el.strip
}

def get_pos pass, idx, low, high
  return high if idx == pass.size

  if pass[idx] == 'F' || pass[idx] == 'L'
    return get_pos(pass, idx+1, low, ((low+high)/2).floor)
  else
    return get_pos(pass, idx+1, ((low+high)/2).ceil, high)
  end
end

max_seat_id = -1

passes.each do |pass|
  row = get_pos(pass[0...7], 0, 0, 127)
  col = get_pos(pass[7...10], 0, 0, 7)
  seat_id = row*8 + col
  max_seat_id = [max_seat_id, seat_id].max
end

puts max_seat_id