import sys
input = sys.stdin.readline

n, c = map(int, input().split())
houses = [int(input()) for _ in range(n)]
houses.sort()
start, end = 1, houses[-1] - houses[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    now = houses[0]
    count = 1

    for i in range(1, len(houses)):
        if now + mid <= houses[i]:
            count += 1
            now = houses[i]

    if count >= c:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(answer)