n = input()
num = sorted(list(map(int, n)), reverse=True)

if 0 in num and sum(num) % 3 == 0:
    for i in num:
        print(i, end='')
else:
    print(-1)