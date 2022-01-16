import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = [], []

for i in range(n):
    for j in range(n):
        ab.append(arr[i][0] + arr[j][1])
        cd.append(arr[i][2] + arr[j][3])

ab.sort()
cd.sort()

i, j = 0, len(cd) - 1
result = 0

while i < len(ab) and j >= 0:
    if ab[i] + cd[j] == 0:
        nexti, nextj = i + 1, j - 1
        # ab가 같은게 여러개인경우
        while nexti < len(ab) and ab[i] == ab[nexti]:
            nexti += 1
        # cd가 같은게 여러개인경우
        while nextj >= 0 and cd[j] == cd[nextj]:
            nextj -= 1

        result += (nexti - i) * (j - nextj)
        i, j = nexti, nextj

    elif ab[i] + cd[j] > 0:
        j -= 1
    else:
        i += 1

print(result)

import sys
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []
ans = 0

for _ in range(n):
    tmp1, tmp2, tmp3, tmp4 = map(int, input().split())
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3)
    d.append(tmp4)

ab = {}

for i in a:
    for j in b:
        if i+j not in ab:
            ab[i+j] = 1
        else:
            ab[i+j] += 1

ans = 0

for i in c:
    for j in d:
        if -(i+j) in ab:
            ans += ab[-(i+j)]

print(ans)

###################################################

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []
ans = 0

for _ in range(n):
    tmp1, tmp2, tmp3, tmp4 = map(int, input().split())
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3)
    d.append(tmp4)

ab = defaultdict(int)

for i in a:
    for j in b:
        ab[i+j] += 1

ans = 0

for i in c:
    for j in d:
        if -(i+j) in ab:
            ans += ab[-(i+j)]

print(ans)

###################################### 시간초과

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
a, b, c, d = [], [], [], []
ans = 0

for i in range(n):
    tmp1, tmp2, tmp3, tmp4 = map(int, input().split())
    a.append(tmp1)
    b.append(tmp2)
    c.append(tmp3)
    d.append(tmp4)

a_b_sum = defaultdict(int)
c_d_sum = defaultdict(int)

for i in a:
    for j in b:
        a_b_sum[i+j] += 1

for i in c:
    for j in d:
        c_d_sum[i+j] += 1

for key in a_b_sum:
    if c_d_sum[-key] != 0:
        ans += (a_b_sum[key] * c_d_sum[-key])

print(ans)

###################################### 시간초과

import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ab, cd = defaultdict(int), defaultdict(int)

for i in range(n):
    for j in range(n):
        ab[arr[i][0] + arr[j][1]] += 1
        cd[arr[i][2] + arr[j][3]] += 1

ab_key = sorted(ab.keys())
cd_key = sorted(cd.keys())

left, right = 0, len(cd_key) - 1
ans = 0

while left < len(ab_key) and right >= 0:
    if ab_key[left] + cd_key[right] == 0:
        ans += (ab[ab_key[left]] * cd[cd_key[right]])
        left += 1
        right -= 1
    elif ab_key[left] + cd_key[right] > 0:
        right -= 1
    else:
        left += 1

print(ans)
