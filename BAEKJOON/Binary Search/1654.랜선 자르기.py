import sys
input = sys.stdin.readline

k, n = map(int, input().split())
array = [int(input()) for _ in range(k)]
start, end = 1, max(array)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for i in array:
        lines += (i // mid)

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)