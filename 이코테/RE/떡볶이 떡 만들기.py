n, m = map(int, input().split())
height = list(map(int, input().split()))

start, end = 0, max(height)
ans = 0

while start <= end:
    mid = (start+end) // 2
    temp = []
    for i in height:
        if i - mid > 0:
            temp.append(i-mid)
        else:
            temp.append(0)

    if sum(temp) >= m:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)