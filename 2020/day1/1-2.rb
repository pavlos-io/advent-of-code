input  = File.readlines('input.txt').map(&:to_i)
target = 2020

# (a[i] + a[j] + a[k] = t) <=> (a[i] + a[j] = t-[k])

def three_sum arr, target
  arr = arr.sort.reverse
  arr.each_with_index do |el, idx|
    r = arr.size - 1
    l = idx + 1
    t = target - el

    while l < r do  
      # print "#{arr[l]} + #{arr[r]} = #{arr[l]+arr[r]}, need #{t} \n"
      if arr[l] + arr[r] == t 
        return el, arr[l], arr[r]
      elsif arr[l] + arr[r] > t 
        l += 1
      else
        r -= 1
      end
    end

  end
end

addends = three_sum(input, target)
puts addends.inject(:*)