require 'set'

input_file = ARGV[0]
commands = File.readlines(input_file, chomp:true).map { |input_line| [(op, num = input_line.split(/ /))[0].to_sym, num.to_i]}

class Puzzle
  @@ops = {
    :nop => -> (num, acc, line) { line, acc = line += 1, acc },
    :acc => -> (num, acc, line) { line, acc = line+1, acc+num },
    :jmp => -> (num, acc, line) { line, acc = line += num, acc }
  }

  def initialize(commands)
    @commands = commands
    @acc = 0
  end

  def terminates?(swap=nil)
    line, visited = 0, Set.new

    while line < @commands.length
      command, val = @commands[line]
      
      if line == swap and swap != nil
        command = command == :nop ? :jmp : :nop
      end
      
      return false if visited.include?(line)
      visited << line    
      line, @acc = @@ops[command].call(val, @acc, line)
    end
    return true
  end

  def run_once
    self.terminates?
    return @acc
  end

  def fix_swapped(swap = 0)
    @acc = 0
    if @commands[swap][0] == :acc
      self.fix_swapped(swap + 1)
    else 
      return @acc if self.terminates?(swap)
      self.fix_swapped(swap + 1)
    end
  end
end

if __FILE__ == $0
  puts Puzzle.new(commands).run_once
  puts Puzzle.new(commands).fix_swapped
end
