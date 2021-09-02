import sys
from collections import Counter
input = sys.stdin.readline


_ = int(input())
n = sorted(list(map(int, input().split())))
_ = int(input())
m = list(map(int, input().split()))

c = Counter(n)

for i in m:
    if i in c.keys():
        print(c[i], end=' ')
    else:
        print(0, end=' ')

