import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
ans = 0

short, long = 1, max(arr)

while short <= long:
    mid = (short + long) // 2
    sum_count = 0
    for i in arr:
        sum_count += (i // mid)
    if sum_count >= n:
        ans = mid
        short = mid + 1
    else:
        long = mid - 1

print(ans)