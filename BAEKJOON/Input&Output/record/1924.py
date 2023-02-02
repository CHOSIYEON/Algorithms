x, y = map(int, input().split())
sum = 0

for i in range(1, x):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        sum += 31
    elif i == 2:
        sum += 28
    else:
        sum += 30
sum += y
sum %= 7

if sum == 1:
    print('MON')
elif sum == 2:
    print('TUE')
elif sum == 3:
    print('WED')
elif sum == 4:
    print('THU')
elif sum == 5:
    print('FRI')
elif sum == 6:
    print('SAT')
else:
    print('SUN')