n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]

data = sorted(data, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(len(data)):
    print(data[i][0])