n, k = map(int, input().split())
arr = [i for i in range(1, n+1)]
idx = 0
answer = []

for i in range(n):
    idx += k - 1
    if idx >= len(arr):
        idx %= len(arr)
    answer.append(str(arr.pop(idx)))

print('<', ', '.join(answer), '>', sep='')
