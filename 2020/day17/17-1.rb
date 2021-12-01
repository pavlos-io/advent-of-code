input = File.read("input.txt").split("\n").map { |row|
  row.split ''
}

def in_bounds? m, i, j, k
  (i >= 0 && i < m.size) &&
  (j >= 0 && j < m.size) && 
  (k >= 0 && k < m.size)
end

def count_adj_active m, i, j, k
  counter = 0

  @dirs.each do |dir|
    x = j + dir[1]
    y = i + dir[0]
    z = k + dir[2]

    if in_bounds?(m, y, x, z) && m[y][x][z] == '#'
      counter += 1
    end
  end

  counter
end

# translates coordinates s.t. negative dimensions are possible
# e.g. if matrix is nxn, then t(0) is n/2 (origin) and t(-n/2) = 0 (left edge)
def t val
  (@sz/2).floor + val
end

@dirs  = []
@sz    = 20
m      = Array.new(@sz) { Array.new(@sz) { Array.new(@sz, '.') } } # x, y, z
origin = Array.new(3, t(0))
half = @sz/2
low = t(-half)
high = t(half)-1 

# get init. state
input.each_with_index do |row, i|
  row.each_with_index do |cell, j|
    m[origin[0]+i][origin[1]+j][t(0)] = cell
  end
end

# generate all directions
[0, 1, -1].each do |i|
  [0, 1, -1].each do |j|
    [0, 1, -1].each do |k|
      next if i==0 && j==0 && k==0
      @dirs << [i, j, k]
    end
  end
end

l = t(-1)
h = t(input.size+1)

(0..5).each do |turn|
  iter = (l..h)
  copy = Marshal.load(Marshal.dump(m))
  iter.each do |i|
    iter.each do |j|
      iter.each do |k|
        cell = m[i][j][k]
        if cell == '#'
          if ![2,3].include? count_adj_active(m, i, j, k)
            copy[i][j][k] = '.'
          end
        else
          if count_adj_active(m, i, j, k) == 3
            copy[i][j][k] = '#'
          end
        end

      end
    end
  end
  l -= 1
  h += 1
  m = copy
end

out = 0
(low..high).each do |i|
  (low..high).each do |j|
    (low..high).each do |k|
      out += 1 if m[i][j][k] == '#'
    end
  end
end

# m.each_with_index do |mat, i|
#   mat.each_with_index do |row, j|
#     print m[i][j][t(-2)]
#   end
#   puts ""
# end

p out