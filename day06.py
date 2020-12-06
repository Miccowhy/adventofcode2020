import sys

input_file = sys.argv[1]
data = open(input_file).read().rstrip().split("\n\n")

print(sum(len(set(group.replace("\n", ''))) for group in data))

print(sum(len(set.intersection(*[set(answers) for answers in group.split("\n")])) for group in data))
