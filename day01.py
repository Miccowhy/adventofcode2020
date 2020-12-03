import sys

input_file = sys.argv[1]

data = [int(element) for element in open(input_file).read().splitlines()]


for i in range(0, len(data)-1):
    for j in range(i+1, len(data)):
        if data[i]+data[j] == 2020:
            print(data[i]*data[j])
            break


for i in range(0, len(data)-2):
    for j in range(i+1, len(data)-1):
        for k in range(i+2, len(data)):
            if data[i]+data[j]+data[k] == 2020:
                print(data[i]*data[j]*data[k])
                break
