import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
answer = []

p1, p2 = 0, 0

while p1 < n and p2 < m:
    if a[p1] >= b[p2]:
        answer.append(b[p2])
        p2 += 1
    else:
        answer.append(a[p1])
        p1 += 1

if p1 < n:
    answer += a[p1:]

if p2 < m:
    answer += b[p2:]

print(' '.join(list(map(str, answer))))