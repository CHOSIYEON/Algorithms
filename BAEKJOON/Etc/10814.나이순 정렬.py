n = int(input())
data = [list(map(str, input().split())) for _ in range(n)]

data = sorted(data, key=lambda x: int(x[0]))

for age, name in data:
    print(age, name)