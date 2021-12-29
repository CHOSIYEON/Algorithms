import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()

low = 1
high = houses[-1] - houses[0]
ans = 0

while low <= high:
    mid = (low + high) // 2
    count = 1
    idx = 0

    for i in range(1, len(houses)):
        if houses[i] - houses[idx] >= mid:
            count += 1
            idx = i

    if count >= c:
        ans = mid
        low = mid + 1
    else:
        high = mid - 1

print(ans)
