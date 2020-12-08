require 'set'

input_file = ARGV[0]
groups = File.read(input_file).split("\n\n")

puts groups.reduce(0) { | sum, group | sum + group.scan(/[a-z]/).uniq.length }

puts groups.reduce(0) { | sum, group |
    sum + group.split.reduce(Set.new('a'..'z')) { | set, answers | set.intersection(answers.scan(/[a-z]/)) }.length }

