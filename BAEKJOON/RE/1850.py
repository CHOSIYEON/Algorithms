a, b = map(int, input().split())

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

ans = gcd(a, b)

for i in range(ans):
    print('1', end='')