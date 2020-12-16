#TODO: Rewrite with Vector!

input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
  [ line[0], line[1..-1].to_i ]
}

def move to, val
  d = to == 'F' ? @dir : @n[to]
  @pos = @pos.map.with_index { |v, i| v + @m[d][i]*val }
end

# def move_ship val
#   @ship_pos = @ship_pos.map.with_index { |v, i| v + @wpt_pos[i]*val }
# end

def turn to, deg
  deg  = to == 'L' ? deg : 360 - deg
  @dir = (@dir + deg/90) % 4;
end

@pos = [0, 0]
@dir = 0

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

  if ['N', 'S', 'E', 'W', 'F'].include? action
    move(action, val)
  else
    turn(action, val)
  end
end

puts @pos[0].abs + @pos[1].abs