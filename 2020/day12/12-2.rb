require 'Matrix'

input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
  [ line[0], line[1..-1].to_i ]
}

def move_wpt to, val
  d = @n[to]
  @wpt_pos = @wpt_pos.map.with_index { |v, i| v + @m[d][i]*val }
end

def move_ship val
  @ship_pos = @ship_pos.map.with_index { |v, i| v + @wpt_pos[i]*val }
end

def turn_wpt to, deg
  deg = to == 'L' ? deg : 360 - deg
  return if deg == 0
  @wpt_pos = ( @rotate[deg] * Matrix.column_vector(@wpt_pos) ).to_a.flatten
end

@ship_pos = [0, 0]
@wpt_pos  = [10, 1]

# Rotates CCW
@rotate = {
  90  => Matrix[ [0,-1], [1,0] ],
  180 => Matrix[ [-1,0], [0,-1] ],
  270 => Matrix[ [0,1], [-1,0] ]
}

@m = {
  0 => [1, 0],
  1 => [0, 1],
  2 => [-1, 0],
  3 => [0, -1]
}

@n = {
  'E' => 0, 
  'N' => 1, 
  'W' => 2, 
  'S' => 3
}

input.each do |instruction|
  action = instruction[0]
  val    = instruction[1]

  if action == 'F'
    move_ship(val)
  elsif ['N', 'S', 'E', 'W'].include? action
    move_wpt(action, val)
  else
    turn_wpt(action, val)
  end
end

puts @ship_pos[0].abs + @ship_pos[1].abs