n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)
ans = 0

while start <= end:
    mid = (start+end) // 2
    total = 0

    for i in arr:
        if i > mid:
            total += i - mid

    if total >= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)