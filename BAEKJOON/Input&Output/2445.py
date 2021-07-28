n = int(input())
sum = 2 * n

for i in range(1, n+1):
    print('*' * i + ' ' * (sum - 2 * i) + '*' * i)

for i in range(n-1, 0, -1):
    print('*' * i + ' ' * (sum - 2 * i) + '*' * i)