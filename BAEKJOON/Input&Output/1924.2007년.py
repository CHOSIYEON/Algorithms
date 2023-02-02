a, b = map(int, input().split())
date = 0
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(a-1, 0, -1):
    if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
        date += 31
    elif i == 4 or i == 6 or i == 9 or i == 11:
        date += 30
    else:
        date += 28

print(day[(date + b) % 7])