import sys

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

a, b = map(int, sys.stdin.readline().split())
n = gcd(a, b)

for i in range(n):
    print(1, end='')