import sys
input = sys.stdin.readline

n, m = map(int, input().split())
trees = list(map(int, input().split()))
short = 1
long = max(trees)
ans = 0

while short <= long:
    mid = (short + long) // 2
    tmp = 0

    for i in trees:
        if i > mid:
            tmp += (i-mid)

    if tmp >= m:
        ans = mid
        short = mid + 1
    else:
        long = mid - 1


print(ans)