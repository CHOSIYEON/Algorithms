def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input().split())

if a >= b:
    ans = gcd(a, b)
else:
    ans = gcd(b, a)

print(ans)
print(a*b//ans)

