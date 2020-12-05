input_file = ARGV[0]
seats = File.readlines(input_file, chomp:true)

ids = []

seats.each do | seat | 
    ids << (seat.tr('FLBR', '0011').to_i(2))
end

puts "#{ids.max}, #{((Array (ids.min..ids.max)) - ids)[0]}"
