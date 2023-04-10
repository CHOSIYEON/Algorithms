n = int(input())
now, count = 1, 1

while n > now:
    now += 6 * count
    count += 1

print(count)