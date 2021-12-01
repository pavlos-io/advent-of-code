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

seat_ids = []

passes.each do |pass|
  row = get_pos(pass[0..6], 0, 0, 127)
  col = get_pos(pass[7..9], 0, 0, 7)
  seat_id = row*8 + col

  seat_ids << seat_id
end

total_sum = (seat_ids.count+1)*(seat_ids.min + seat_ids.max)/2
puts total_sum - seat_ids.sum


