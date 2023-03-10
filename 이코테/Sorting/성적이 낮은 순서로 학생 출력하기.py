n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]

data.sort(key=lambda x: int(x[1]))

for i in data:
    print(i[0], end=' ')
