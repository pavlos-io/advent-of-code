input = File.readlines('input.txt')
input = input.map {|el| el.split(" ")}

def count_valid_passwords input
  counter = 0
  
  input.each do |row|
    min, max = row[0].split("-").map(&:to_i)

    if is_valid_password?(min, max, row[1][0], row[2])
      counter += 1
    end
  end

  counter
end



def is_valid_password? min, max, letter, password
  c = password.count(letter)
  return (c >= min) && (c <= max)
end

puts count_valid_passwords input