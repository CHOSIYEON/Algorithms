arr = list(map(int, input()))
ans = arr[0]

for i in range(1, len(arr)):
    num = arr[i]
    if arr[i] <= 1 or ans <= 1:
        ans += num
    else:
        ans *= num

print(ans)