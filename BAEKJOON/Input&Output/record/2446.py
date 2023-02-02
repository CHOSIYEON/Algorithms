n = int(input())
sum = 2 * n

for i in range(n, 0, -1):
    star = 2 * i - 1
    print(' ' * ((sum-star)//2) + '*' * star)

for i in range(2, n+1):
    star = 2 * i - 1
    print(' ' * ((sum-star)//2) + '*' * star)

