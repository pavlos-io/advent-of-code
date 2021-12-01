input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
}.select{ |line|
  !line.include?(" no ") #exclude leaves
}

def build_graph input
  adj_list = {}
  input.each do |line|
    line = line.split("contain")
    node = line[0].split(' ')
    node = "#{node[0]} #{node[1]}"
    adj_list[node] = []
    
    edges = line[1].split(',')
    edges.each do |e|
      e = e.split(' ')
      adj_list[node] << "#{e[1]} #{e[2]}"
    end
  end
  adj_list
end

def dfs node, g, can, target
  return true      if node == target
  return false     if g[node].nil? #for nodes that are leaves
  return can[node] if !can[node].nil? #visited
  
  can_fit_target = false
  g[node].each do |nbr|
    can_fit_target = dfs(nbr, g, can, target)
    break if can_fit_target
  end

  can[node] = can_fit_target
  return can_fit_target
end

def main input
  target  = "shiny gold"
  can     = {}
  g       = build_graph input

  g.each do |node, nbrs|
    next if node == target # don't need to dfs this node
    dfs(node, g, can, target)
  end

  return can.count { |k,v| v == true }
end

puts main(input)