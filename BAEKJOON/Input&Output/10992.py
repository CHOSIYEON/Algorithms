n = int(input())
sum = 2 * n - 1

for i in range(1, n):
    star = 2 * i - 1
    if i == 1:
        print(' ' * ((sum - star) // 2) + '*' + ' ' * (star - 2) )
    else:
        print(' ' * ((sum - star) // 2) + '*' + ' ' * (star - 2) + '*')

print('*' * sum)