a, b = map(int, input().split())

for i in range(min(a,b), 0, -1):
    if a % i == 0 and b % i == 0:
        print(i)
        break

for i in range(max(a,b), (a*b)+1):
    if i % a == 0 and i % b == 0:
        print(i)
        break

# 유클리드호제
a, b = map(int, input().split())

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x*y) // gcd(x, y)

print(gcd(a, b))
print(lcm(a, b))