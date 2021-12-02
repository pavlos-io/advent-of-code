input = File.readlines("input.txt").map{ |line|
  line.gsub("\n", '')
}.select{ |line|
  !line.include?(" no ") #exclude leaves
}

def build_weighted_graph input
  adj_list = {}
  input.each do |line|
    line = line.split("contain")
    node = line[0].split(' ')
    node = "#{node[0]} #{node[1]}"
    adj_list[node] = []
    
    edges = line[1].split(',')
    edges.each do |e|
      e = e.split(' ')
      adj_list[node] << ["#{e[1]} #{e[2]}", e[0].to_i]
    end
  end
  adj_list
end

def dfs node, g, count
  return 0           if g[node].nil? #for nodes that are leaves
  return count[node] if !count[node].nil? #visited

  counter = 0

  g[node].each do |edge|
    nbr = edge[0]
    wt = edge[1]
    counter += wt + wt*dfs(nbr, g, count)
  end

  count[node] = counter
  return counter
end

def main input
  target  = "shiny gold"
  count   = {}
  g       = build_weighted_graph input

  return dfs(target, g, count)
end


puts main(input)