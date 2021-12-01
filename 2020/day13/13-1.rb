input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
}

timestamp = input[0].to_i
bus_ids   = input[1].split(',').reject { |id| id == 'x' }.map(&:to_i)

waiting_time = {}

bus_ids.each do |id|
  t = 0
  while t < timestamp do
    t += id
  end
  waiting_time[id] = t - timestamp
end

puts waiting_time.min_by{|k, v| v}.inject(:*)