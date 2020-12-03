import sys
import math

input_file = sys.argv[1]

data = [line for line in open(input_file).read().splitlines()]

trees = []
slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
for right, down in slopes:
   i = 0; j = 0
   counter = 0
   while i in range(len(data)-down):
       if data[(i := i+down)][(j := (j+right) % len(data[0]))] == '#': counter += 1
   trees.append(counter)
print(f"{trees[1]}, {math.prod(trees)}")
