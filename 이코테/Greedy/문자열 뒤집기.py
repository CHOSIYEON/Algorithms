arr = list(map(int, input()))
cnt = [0, 0]
ans = 0

current = arr[0]

for i in range(1, len(arr)):
    if current != arr[i]:
        cnt[current] += 1
        current = arr[i]

cnt[arr[-1]] += 1
print(min(cnt))