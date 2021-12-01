input = File.readlines('input.txt')
input = input.map {|el| el.split(" ")}

def count_valid_passwords input
  counter = 0
  
  input.each do |row|
    i, j = row[0].split("-").map(&:to_i)

    if is_valid_password?(i, j, row[1][0], row[2])
      counter += 1
    end
  end

  counter
end



def is_valid_password? i, j, letter, password
  return (password[i-1] == letter) ^ (password[j-1] == letter)
end

puts count_valid_passwords input