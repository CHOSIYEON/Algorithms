n, m = map(int, input().split())
min_value = []

for i in range(n):
    tmp = list(map(int, input().split()))
    min_value.append(min(tmp))

print(max(min_value))
