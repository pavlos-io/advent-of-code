class Calc
  def self.compute idx, problem
    sum = num = 0
    sign = '+'

    while idx < problem.size do
      c = problem[idx]
      if c == '('
        idx += 1
        num, idx = self.compute idx, problem
        next
      end

      if c.match(/[0-9]/)
        num = num*10 + c.to_i
      end
      
      if !c.match(/[0-9]/) || idx == problem.size-1 || c == ')'
        if sign == '+' 
          sum += num
        else 
          sum *= num
        end
        num = 0;
        sign = c;
      end
      idx += 1
      break if c == ')' 
    end

    if sign == '+' 
      sum += num
    elsif sign == '*'
      sum *= num
    end
    
    [sum, idx]
  end
end