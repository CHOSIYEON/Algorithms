n = int(input())
m = int(input())

enable_controller = {str(i) for i in range(10)}

if m != 0:
    enable_controller-=set(map(str, input().split()))

min_cnt = abs(100 - n)

for channel in range(1000000):
    for j in range(len(str(channel))):
        if str(channel)[j] not in enable_controller:
            break
        elif len(str(channel)) - 1 == j:
            min_cnt = min(min_cnt, abs(channel - n) + len(str(channel)))
print(min_cnt)    