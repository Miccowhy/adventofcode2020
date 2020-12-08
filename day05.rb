input_file = ARGV[0]
seats = File.readlines(input_file, chomp:true).map { |seat| seat.tr('FLBR', '0011').to_i(2) }

puts "#{seats.max}, #{((Array (seats.min..seats.max)) - seats)[0]}"
