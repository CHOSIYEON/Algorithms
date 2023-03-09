n = int(input())
data = list(map(int, input().split()))
start, end = 0, len(data) - 1
answer = False

while start <= end:
    mid = (start + end) // 2

    if data[mid] == mid:
        answer = True
        break
    elif data[mid] > mid:
        end = mid - 1
    else:
        start = mid + 1

if answer:
    print(mid)
else:
    print(-1)
