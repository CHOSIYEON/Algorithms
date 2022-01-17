import sys
input = sys.stdin.readline
from collections import Counter

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = 0

a_sum = []
b_sum = []

for i in range(n):
    tmp = 0
    for j in range(i, n):
        tmp += a[j]
        a_sum.append(tmp)

for i in range(m):
    tmp = 0
    for j in range(i, m):
        tmp += b[j]
        b_sum.append(tmp)

a_sum.sort()
b_sum.sort()

c = Counter(b_sum)

for i in a_sum:
    ans += c[t-i]

print(ans)

################################### 메모리 초과 - sum

import sys
input = sys.stdin.readline
from collections import defaultdict

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
ans = 0

a_sum = defaultdict(int)
b_sum = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        a_sum[sum(a[i:j+1])] += 1

for i in range(m):
    for j in range(i, m):
        b_sum[sum(b[i:j+1])] += 1

for key in a_sum.keys():
    ans += (a_sum[key] * b_sum[t-key])

print(ans)
