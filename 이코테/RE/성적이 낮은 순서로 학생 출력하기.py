n = int(input())
data = []

for _ in range(n):
    name, score = map(str, input().split())
    data.append((name, int(score)))

data.sort(key = lambda x: x[1])

for i in data:
    print(i[0], end = ' ')