n, m = map(int, input().split())
total = 0

if n == 1:
    total = 1
elif n == 2:
    total = min(3, (m-1)//2) + 1
elif n >= 3 and m < 7:
    total = min(3, m-1) + 1
else:
    total = 2 + m - 5 + 1

print(total)