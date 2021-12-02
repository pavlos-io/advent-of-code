input = File.readlines("input.txt")[1].
  split(',').map.with_index{ |el, idx|
    [idx, el == 'x' ? -1 : el.to_i]
}.to_h.reject { |k, v| v == -1 }

# https://github.com/acmeism/RosettaCodeData/blob/master/Task/Chinese-remainder-theorem/Ruby/chinese-remainder-theorem-2.rb
def extended_gcd(a, b)
  last_remainder, remainder = a.abs, b.abs
  x, last_x, y, last_y = 0, 1, 1, 0
  while remainder != 0
    last_remainder, (quotient, remainder) = remainder, last_remainder.divmod(remainder)
    x, last_x = last_x - quotient*x, x
    y, last_y = last_y - quotient*y, y
  end
  return last_remainder, last_x * (a < 0 ? -1 : 1)
end

def invmod(e, et)
  g, x = extended_gcd(e, et)
  if g != 1
    raise 'Multiplicative inverse modulo does not exist!'
  end
  x % et
end

def chinese_remainder(mods, remainders)
  max = mods.inject( :* )  # product of all moduli
  series = remainders.zip(mods).map{ |r,m| (r * max * invmod(max/m, m) / m) }
  series.inject( :+ ) % max
end

puts (chinese_remainder(input.values, input.keys) - input.values.inject(:*)).abs

# t = 0 mod(7)
# t = 1 mod(13)
# t = 4 mod(59)
# t = 6 mod(31)
# t = 7 mod(19)
