n = int(input())
sum = int(2 * n - 1)
for i in range(1, n+1):
    side = int((sum - (2 * i - 1))/2)
    print(' ' * side + '*' * (2 * i - 1))