n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]

data = sorted(data, key=lambda x:(x[0], x[1]))

for x, y in data:
    print(x, y)