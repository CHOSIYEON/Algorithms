t = int(input())

def gcd(x, y):
    while y != 0:
        x, y = y, x%y
    return x

for i in range(t):
    x, y = map(int, input().split())
    if x>=y:
        print(x*y//gcd(x, y))
    else:
        print(x*y//gcd(y, x))