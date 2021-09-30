import sys
input = sys.stdin.readline

r, c = map(int, input().split())
arr = []

for i in range(r):
   temp = list(map(int, input().split()))
   arr.append(temp)

if r % 2 == 0:
    if c>=4:
        max=r+c
    else:
        max = r+c-2
    current_x, current_y = 0, 0
    count = 0
    while count < max:
        if current_y == 0 and current_x != c-1:
            if arr[current_x][current_y+1] >= arr[current_x+1][current_y]:
                print('R',end='')
                current_y += 1
                count += 1
            else:
                print('D',end='')
                current_x += 1
                count += 1
        elif current_y == r-1 and current_x != c-1:
            if arr[current_x][current_y-1] >= arr[current_x+1][current_y]:
                print('L', end='')
                current_y -= 1
                count += 1
            else:
                print('D', end='')
                current_x += 1
                count += 1
        elif current_x == c-1:
            print('R', end='')
            current_y += 1
            count += 1
        else:
            left = arr[current_x][current_y-1]
            right = arr[current_x][current_y+1]
            down = arr[current_x+1][current_y]

            if left >= right and left >= down:
                print('L', end='')
                current_y -= 1
                count += 1
            elif right >= left and right >= down:
                print('R', end='')
                current_y += 1
                count += 1
            elif down >= right and down >= left:
                current_x += 1
                count += 1
else:
    for i in range(r):
        for j in range(c-1):
            if i % 2 == 0:
                print('R', end='')
            else:
                print('L', end='')
        if i != r-1:
            print('D', end='')