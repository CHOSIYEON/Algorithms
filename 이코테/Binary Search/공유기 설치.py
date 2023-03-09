import sys
input = sys.stdin.readline

n, c = map(int, input().split())
data = [int(input()) for _ in range(n)]
data.sort()
start, end = 1, data[-1] - data[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    value = data[0]
    count = 1

    for i in range(1, len(data)):
        if value + mid <= data[i]:
            count += 1
            value = data[i]

    if count >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)