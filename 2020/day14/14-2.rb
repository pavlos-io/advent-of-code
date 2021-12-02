input = File.read("input.txt").split("mask").drop(1).map{|el| el.split("\n")}

# 1. Gets the address after applying mask (Xs are left as is)
# 2. Replace every X with a '0' and remember where the Xs were
# 3. Take the bin. rep. of numbers 0 thru 2^(# of Xs)-1 and replace the known indices w/ the rep.
def apply_mask num, mask
  floating_addr = get_floating_num num, mask 
  n             = floating_addr.count('X')
  all           = []
  
  return [floating_addr.to_i(2)] if n == 0

  x_indices = floating_addr.split('').each_index.select{|i| floating_addr[i] == 'X'}
  num2      = floating_addr.gsub('X', '0')

  (0..(1<<n)-1).each do |el|
    bits = el.to_s(2).reverse

    bits.split('').each_with_index do |b, idx|
      num2[ x_indices[idx] ] = b
    end
    all.push num2.to_i(2)
  end
  all
end

def get_floating_num num, mask 
  out = ""
  num_s = num.to_s(2).reverse
  mask = mask.reverse
  i = 0
  while i < num_s.size do
    if mask[i] == '0'
      mask[i] = num_s[i]
    end
    i += 1
  end
  mask.reverse
end

mem = {}

input.each do |program|
  mask = ""
  program.each do |line|
    if line[0..2] == "mem"
      addr = line.split(" =")[0].scan(/\d/).join('').to_i
      num  = line.split("= ")[1].to_i
      all  = apply_mask(addr, mask)
      all.each do |a|
        mem[a] = num
      end
    else
      mask = line.split("= ")[1]
    end
  end
end

p mem.values.sum