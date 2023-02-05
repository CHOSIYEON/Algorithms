import sys
input = sys.stdin.readline

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

t = int(input())

for n in range(t):
    arr = list(map(int, input().split()))
    m = arr.pop(0)
    sum = 0

    for i in range(m):
        for j in range(m):
            if i < j:
                sum += gcd(arr[i], arr[j])
    print(sum)