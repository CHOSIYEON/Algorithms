import sys
input = sys.stdin.readline

n = int(input())
ans = 0
minus = []
plus = []
zero = False
one = 0

for i in range(n):
    n = int(input())
    if n > 1:
        plus.append(n)
    elif n < 0:
        minus.append(n)
    elif n == 0:
        zero = True
    elif n == 1:
        one += 1

minus.sort()
plus.sort(reverse=True)

if minus:
    if len(minus) % 2 == 0:
        for i in range(0, len(minus), 2):
            ans += (minus[i] * minus[i + 1])
    else:
        for i in range(0, len(minus) - 1, 2):
            ans += (minus[i] * minus[i + 1])
        if not zero:
            ans += minus[-1]

if plus:
    if len(plus) % 2 == 0:
        for i in range(0, len(plus), 2):
            ans += (plus[i] * plus[i + 1])
    else:
        for i in range(0, len(plus) - 1, 2):
            ans += (plus[i] * plus[i + 1])
        ans += plus[-1]

print(ans + one)

