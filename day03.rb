input_file = ARGV[0]

data = File.readlines(input_file, chomp:true)

trees = []
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]


slopes.each do | right, down |
    i = j = counter = 0
    while i < (data.length - down)
        counter += 1 if data[(i = i + down)][(j = (j + right) % data[0].length())] == '#'
    end
    trees << counter
end
puts "#{trees[1]}, #{trees.reduce(:*)}"
