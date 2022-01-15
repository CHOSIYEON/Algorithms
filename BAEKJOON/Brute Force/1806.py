import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))
left, right = 0, 0
sum_num = 0
ans = sys.maxsize

while True:
    if sum_num >= s:
        ans = min(ans, right-left)
        sum_num -= arr[left]
        left += 1
    elif right == n:
        break
    else:
        sum_num += arr[right]
        right += 1


if ans == sys.maxsize:
    print(0)
else:
    print(ans)