import sys

input_file = sys.argv[1]
seats = [line for line in open(input_file).read().splitlines()]

ids = []
for seat in seats:
    binary = seat.translate('FBRL'.maketrans({'F': '0', 'B': '1', 'R': '1', 'L': '0'}))
    ids.append(int(binary, 2))

print(f"{max(ids)}, {set(range(min(ids), max(ids))) - set(ids)}")
    
