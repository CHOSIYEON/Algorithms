import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 1
ans = 0

while left <= right <= n:
    sum_num = sum(arr[left:right])

    if sum_num == m:
        ans += 1
        right += 1
    elif sum_num < m:
        right += 1
    elif sum_num > m:
        left += 1

print(ans)
