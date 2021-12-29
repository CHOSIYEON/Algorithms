import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
cards2 = list(map(int, input().split()))

c = Counter(cards)

for i in cards2:
    if i in c.keys():
        print(c[i], end=' ')
    else:
        print(0, end=' ')