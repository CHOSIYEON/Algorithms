n, m = map(int, input().split())
data = list(map(int, input().split()))
start, end = 0, max(data)
answer = 0

while start <= end:
    mid = (start + end) // 2
    summary = 0

    for i in range(len(data)):
        if data[i] - mid > 0:
            summary += (data[i] - mid)

    if summary >= m:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)