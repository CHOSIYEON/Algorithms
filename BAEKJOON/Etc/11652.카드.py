import sys
input = sys.stdin.readline

n = int(input())
data = [int(input()) for _ in range(n)]
data_dict = {}

for num in data:
    if num in data_dict.keys():
        data_dict[num] += 1
    else:
        data_dict[num] = 1

data_dict = sorted(data_dict.items(), key=lambda x:(-x[1], x[0]))

print(data_dict[0][0])
