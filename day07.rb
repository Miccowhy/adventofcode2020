require 'set'

input_file = ARGV[0]
$bags = File.readlines(input_file, chomp:true).map { |line| [(bag = line.scan(/\w+ \w+(?= bag)/))[0].to_sym, bag[1..-1].map(&:to_sym).to_set] }.to_h

def find_bag_containing(color)
  colors = $bags.select { | bag, content | content.include?(color)}.map{ | bag, content | bag }.to_set
  return colors | colors.each.map { |next_color| find_bag_containing(next_color) }.to_set if colors.any?
end

# Sliver star only for now
puts find_bag_containing(:'shiny gold').flatten.delete(nil).length
