grid = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '').split('')
}

EMPTY = 'L'
OCCUP = '#'
FLOOR = '.'
DIRS  = [ 
  [1,0], [0,1], [-1,0], [0,-1], 
  [1,1], [1,-1], [-1,1], [-1,-1]
]

def in_bounds?(grid, x, y)
  (x >= 0) && (y >= 0) && (x < grid[0].count) && (y < grid.count)
end

def adj_occupied(grid, i, j)
  occupied_seats = 0

 
  DIRS.each do |dir|
    x = j
    y = i
    while grid[i][j] != FLOOR do
      x = x + dir[0]
      y = y + dir[1]
      if in_bounds?(grid, x, y)
        
        if grid[y][x] == OCCUP
          occupied_seats += 1
          break
        elsif grid[y][x] == EMPTY
          break
        end

      else
        break
      end
    end
  end

  occupied_seats
end

def count_empty_seats grid
  counter = 0

  grid.each do |row|
    row.each do |cell|
      counter += 1 if cell == OCCUP
    end
  end

  counter
end

# def print_grid grid
#   grid.each do |row|
#     print row, "\n"
#   end
#   print "\n"
#   print "\n"
# end

ok   = true
iter = 0

while ok do
  ok    = false
  iter += 1
  copy  = grid.map(&:clone)

  grid.each_with_index do |row, i|
    row.each_with_index do |cell, j|
      
      if cell == EMPTY && adj_occupied(grid, i , j) == 0
        copy[i][j] = OCCUP
        ok = true
      elsif cell == OCCUP && adj_occupied(grid, i , j) >= 5
        copy[i][j] = EMPTY
        ok = true
      end

    end
  end

  grid = copy
end

puts iter-1, count_empty_seats(grid)