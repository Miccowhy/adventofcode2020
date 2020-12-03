import sys
import re

input_file = sys.argv[1]

data = [line for line in open(input_file).read().splitlines()]

counter_one, counter_two = [0, 0] 
for line in data:
    l_bound, h_bound, letter, word = re.split('-|: | ', line)
    l_bound, h_bound = [int(l_bound), int(h_bound)]
    if l_bound <= word.count(letter) <= h_bound: counter_one += 1
    if (letter == word[l_bound-1]) ^ (letter == word[h_bound-1]): counter_two += 1
print(f"{counter_one}, {counter_two}")
